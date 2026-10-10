"""Reconstruct reference edges from a bounded local mbox, omitting private content."""
import argparse, hashlib, json, mailbox, pathlib, re
ID=re.compile(r"<[^<>\s]+>")
def build(messages):
    nodes={};missing_ids=0
    def digest(x): return hashlib.sha256(x.encode("utf-8")).hexdigest()
    for index,msg in enumerate(messages):
        if index>=10000: raise ValueError("more than 10000 messages")
        ids=ID.findall(str(msg.get("Message-ID","")))
        if len(ids)!=1 or len(msg.get_all("Message-ID",[]))!=1:
            missing_ids+=1;continue
        ident=ids[0]
        if ident in nodes: raise ValueError("duplicate Message-ID")
        refs=ID.findall(" ".join(str(v) for v in msg.get_all("References",[])))
        reply=ID.findall(" ".join(str(v) for v in msg.get_all("In-Reply-To",[])))
        if len(refs)>1000 or len(reply)>1000: raise ValueError("reference header exceeds bound")
        nodes[ident]={"index":index,"refs":refs,"reply":reply}
    edges={};findings=[]
    for ident,n in nodes.items():
        candidates=n["refs"] or n["reply"]
        if candidates:
            parent=candidates[-1];edges[ident]=parent
            if parent==ident: findings.append({"code":"self-reference","id":digest(ident)})
            elif parent not in nodes: findings.append({"code":"missing-parent","child":digest(ident),"parent":digest(parent)})
    done=set();cycles=[]
    for start in nodes:
        if start in done: continue
        chain=[];positions={};cur=start
        while cur in nodes and cur not in done and cur not in positions:
            positions[cur]=len(chain);chain.append(cur);cur=edges.get(cur)
        if cur in positions:
            cycle=chain[positions[cur]:];cycles.append(sorted(digest(v) for v in cycle))
        done.update(chain)
    for cycle in cycles: findings.append({"code":"cycle","ids":cycle})
    if missing_ids: findings.append({"code":"missing-or-ambiguous-message-id","count":missing_ids})
    children={x:[] for x in nodes}
    for child,parent in edges.items():
        if parent in children:children[parent].append(child)
    components=[];visited=set()
    for start in sorted(nodes):
        if start in visited:continue
        stack=[start];members=[]
        while stack:
            cur=stack.pop()
            if cur in visited:continue
            visited.add(cur);members.append(cur);stack.extend(children[cur])
            parent=edges.get(cur)
            if parent in nodes:stack.append(parent)
        components.append(sorted(digest(x) for x in members))
    return {"ok":not findings,"message_count":len(nodes)+missing_ids,"identified_count":len(nodes),"edges":[{"child":digest(c),"parent":digest(p),"parent_present":p in nodes} for c,p in sorted(edges.items())],"components":components,"findings":findings}
def inspect(path):
    path=pathlib.Path(path)
    if not path.is_file():raise ValueError("mbox must be an existing regular file")
    if path.stat().st_size>32*1024*1024:raise ValueError("mbox exceeds 32 MiB")
    if path.stat().st_size and not path.read_bytes().startswith(b"From "):raise ValueError("missing mbox envelope")
    box=mailbox.mbox(str(path),create=False)
    try:return build(box)
    finally:box.close()
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("mbox");a=p.parse_args()
    try:r=inspect(a.mbox);print(json.dumps(r));return 0 if r["ok"] else 1
    except (ValueError,OSError,mailbox.Error) as e:print(json.dumps({"error":str(e)}));return 2
if __name__=="__main__":raise SystemExit(main())

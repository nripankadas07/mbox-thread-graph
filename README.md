# mbox-thread-graph

Read a local mbox, select the last References ID or In-Reply-To fallback, expose missing/cyclic edges and connected thread components, with full SHA-256 IDs and no subjects, addresses or bodies.

## Who and why

Mail archive maintainers examining exported mbox thread structure without publishing message contents. Missing parents, reused Message-IDs and reference cycles make migrated conversations ambiguous. A GUI view can conceal which exact reference edge determined a thread.

## Quickstart

Python 3.10+ and pip. No service, credential or runtime dependency:

```sh
git clone https://github.com/nripankadas07/mbox-thread-graph.git
cd mbox-thread-graph
python -m venv .venv
# Unix: source .venv/bin/activate; Windows: .venv\Scripts\activate
python -m pip install .
mbox-thread-graph sample.mbox
python demo.py
python -m pip install setuptools wheel
python verify.py
```

The fixtures are synthetic. CLI JSON is on stdout. Exit 0 means the operation succeeded; HLS/mbox return 1 for findings; all tools return 2 for malformed/unsupported input or IO errors. SQLite scan signals are evidence, not policy failures. PNG output must be a new file: repeating its command requires a new output filename.

Help: `mbox-thread-graph --help`. See [DEMO.md](DEMO.md), [VALIDATION.md](VALIDATION.md), [RESEARCH.md](RESEARCH.md) and [SUPPORT.md](SUPPORT.md).

## Scope and limitations

No mailbox writing, IMAP, MIME rendering, subject-based grouping, JWZ dummy-container merging or RFC header certification. Angle-bracket tokens are used as IDs; malformed/ambiguous/missing Message-ID records produce findings and cannot be placed in a component. Duplicate IDs reject the input. Last declared parent is selected even if absent; missing intermediate References entries are not diagnosed. Case-sensitive IDs. Hashes are pseudonyms and can be guessed; reports can reveal relationships. The file must remain stable during inspection. 32 MiB, 10,000 messages and 1,000 reference IDs/header.

No performance-superiority or complete-security claim. Use the comparable research to choose a tool suitable for your workflow.

## License

MIT; original implementation. Build-time setuptools/wheel and Python retain their upstream licenses.

import email,unittest,tempfile,pathlib
from mbox_thread_graph import build,inspect
def msg(ident=None,refs=None,reply=None):
    raw="Subject: secret subject\nFrom: private@example.com\n"
    if ident is not None:raw+="Message-ID: "+ident+"\n"
    if refs is not None:raw+="References: "+refs+"\n"
    if reply is not None:raw+="In-Reply-To: "+reply+"\n"
    return email.message_from_string(raw+"\nprivate body")
class Contract(unittest.TestCase):
    def test_chain(self):
        r=build([msg("<a@x>"),msg("<b@x>","<a@x>"),msg("<c@x>","<a@x> <b@x>")]);self.assertTrue(r["ok"]);self.assertEqual(len(r["components"]),1);self.assertEqual(len(r["edges"]),2)
    def test_fallback(self):self.assertEqual(len(build([msg("<a@x>"),msg("<b@x>",reply="<a@x>")])["components"]),1)
    def test_references_precedence(self):self.assertTrue(build([msg("<a@x>"),msg("<b@x>","<a@x>","<absent@x>")])["ok"])
    def test_missing(self):self.assertEqual(build([msg("<a@x>","<absent@x>")])["findings"][0]["code"],"missing-parent")
    def test_cycle(self):self.assertTrue(any(f["code"]=="cycle" for f in build([msg("<a@x>","<b@x>"),msg("<b@x>","<a@x>")])["findings"]))
    def test_self(self):self.assertFalse(build([msg("<a@x>","<a@x>")])["ok"])
    def test_duplicate(self):
        with self.assertRaises(ValueError):build([msg("<a@x>"),msg("<a@x>")])
    def test_missing_id(self):self.assertEqual(build([msg()])["identified_count"],0)
    def test_ambiguous_id(self):self.assertFalse(build([msg("<a@x> <b@x>")])["ok"])
    def test_privacy(self):
        r=str(build([msg("<a@x>")]));self.assertNotIn("secret subject",r);self.assertNotIn("private",r);self.assertNotIn("<a@x>",r)
    def test_disconnected(self):self.assertEqual(len(build([msg("<a@x>"),msg("<b@x>")])["components"]),2)
    def test_empty(self):self.assertTrue(build([])["ok"])
    def test_real_mbox(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/"mail";p.write_text("From synthetic@example.com Sat Jan 1 00:00:00 2026\nMessage-ID: <a@x>\n\nbody\n")
            self.assertEqual(inspect(p)["message_count"],1)
    def test_missing_file_not_created(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/"absent"
            with self.assertRaises(ValueError):inspect(p)
            self.assertFalse(p.exists())

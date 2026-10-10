# Synthetic demo

Run `python demo.py` to exercise the checked-in synthetic fixture, expected success/evidence and malformed input using `smoke.json`.

Installed command: `mbox-thread-graph sample.mbox`. Each smoke case records its exact expected exit and any essential output fields. Policies/input schemas follow the fixture files and module docstring; no private input is included.

No mailbox writing, IMAP, MIME rendering, subject-based grouping, JWZ dummy-container merging or RFC header certification. Angle-bracket tokens are used as IDs; malformed/ambiguous/missing Message-ID records produce findings and cannot be placed in a component. Duplicate IDs reject the input. Last declared parent is selected even if absent; missing intermediate References entries are not diagnosed. Case-sensitive IDs. Hashes are pseudonyms and can be guessed; reports can reveal relationships. The file must remain stable during inspection. 32 MiB, 10,000 messages and 1,000 reference IDs/header.

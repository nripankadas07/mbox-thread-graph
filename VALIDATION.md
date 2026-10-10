# Validation — 10 October 2026

Acceptance suite: 14 meaningful core tests, module compilation, synthetic demo, wheel build and new-venv console commands outside source. Run `python verify.py`. No competitor benchmark was performed.

Remote CI is required before LIVE; receipts are recorded in the owner's chronological index. Supported matrix: Ubuntu/Python 3.10, 3.12, 3.14. Other OS/architectures are untested. Build tools must be available to run verification; the normal install path uses pip build isolation.

No mailbox writing, IMAP, MIME rendering, subject-based grouping, JWZ dummy-container merging or RFC header certification. Angle-bracket tokens are used as IDs; malformed/ambiguous/missing Message-ID records produce findings and cannot be placed in a component. Duplicate IDs reject the input. Last declared parent is selected even if absent; missing intermediate References entries are not diagnosed. Case-sensitive IDs. Hashes are pseudonyms and can be guessed; reports can reveal relationships. The file must remain stable during inspection. 32 MiB, 10,000 messages and 1,000 reference IDs/header.

Local observed result: all acceptance checks passed on Linux/Python 3.12 with setuptools 84.0.0 and wheel 0.48.0. A new wheel environment, outside-source CLI success/failure checks and the synthetic demo passed. Remote matrix and normal build-isolated installation must still be verified at the public final commit.

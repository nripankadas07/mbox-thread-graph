# Research and candidate brief — 10 October 2026

User: Mail archive maintainers examining exported mbox thread structure without publishing message contents.

Pain: Missing parents, reused Message-IDs and reference cycles make migrated conversations ambiguous. A GUI view can conceal which exact reference edge determined a thread.

Smallest useful capability: Read a local mbox, select the last References ID or In-Reply-To fallback, expose missing/cyclic edges and connected thread components, with full SHA-256 IDs and no subjects, addresses or bodies.

Demand is **inferred** from the workflow and established alternatives, not a verified request for this project. No invented users, adoption or growth promise.

Queries: `mbox sort:stars`, GitHub repository search with stars qualifier, bounded first five results plus named relevant established comparables. Connector coverage and relevance selection are limited; this is not an exhaustive ranking. Highest-star relevant comparable **among those inspected**: [neomutt/neomutt](https://github.com/neomutt/neomutt) (3848 stars). Stars are research context, not technical performance.

| Exact comparable | Observed stars | Last push UTC | API license metadata |
| --- | ---: | --- | --- |
| [neomutt/neomutt](https://github.com/neomutt/neomutt) | 3848 | 2026-10-05T00:54:58Z | GPL-2.0 |
| [jstedfast/MimeKit](https://github.com/jstedfast/MimeKit) | 2006 | 2026-10-10T02:57:58Z | MIT |
| [meli/meli](https://github.com/meli/meli) | 898 | 2026-10-08T13:07:45Z | GPL-3.0 |

Observed 10 October 2026 via GitHub repository metadata, current README and first five open issues. Missing README/license metadata is unavailable rather than evidence of absent support; NOASSERTION requires manual license review before any reuse. No reuse occurred. Archived status is preserved in raw research evidence; grafov/m3u8's README identifies its successor and suspended support.

Fair comparison: established alternatives have broader parsing, client, GUI, optimization, binding or management workflows and should be considered first. This tool offers the bounded offline workflow in the capability above, a Python source installation, synthetic example and exact failure exits. Its zero runtime dependencies do not establish better reliability or support. Installation and time-to-first-result were measured only for our examples; competitor installations and equivalent workloads were not benchmarked. We make no absence or superiority claim. Compare the stated scope/limitations with each alternative's current docs before selecting it.

Portfolio differentiation: rssdeck handles syndication; pigeon messaging is a different workflow. This reconstructs offline mail reference graphs rather than sending mail. The other four daily projects use different data, algorithms and users (video windows, mail graphs, SQL plans, PNG bytes, numeric ACLs); they are not subdivisions of one product.

Acceptance: the documented example produces its expected evidence; meaningful malformed inputs fail; original core behavior/regressions pass 14 tests; installed console command works outside source; remote CI runs Python 3.10, 3.12 and 3.14. Public existence without these checks is not a verified launch.

Discovery: mbox and email-archive topics plus a synthetic threaded archive example.

Limits: No mailbox writing, IMAP, MIME rendering, subject-based grouping, JWZ dummy-container merging or RFC header certification. Angle-bracket tokens are used as IDs; malformed/ambiguous/missing Message-ID records produce findings and cannot be placed in a component. Duplicate IDs reject the input. Last declared parent is selected even if absent; missing intermediate References entries are not diagnosed. Case-sensitive IDs. Hashes are pseudonyms and can be guessed; reports can reveal relationships. The file must remain stable during inspection. 32 MiB, 10,000 messages and 1,000 reference IDs/header.

## Workflow comparison

NeoMutt and meli are interactive mail clients with mailbox/thread navigation, configuration and wider mail workflows. MimeKit is a .NET MIME/mail library with package installation and library integration rather than this Python CLI contract. Their mature documentation and support histories exceed this MVP's small fixture/Issues workflow. Our first result is a local mbox graph report; it deliberately does not display/send mail or fully implement client threading. No claim that these alternatives cannot expose reference information; their exact behavior was not benchmarked.

Evidence observed between 06:12 and 06:22 UTC, 10 October 2026. Repository metadata is a snapshot; push time is activity evidence, not a support guarantee.

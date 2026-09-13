<!-- Copyright © 2026 Manolo Remiddi · SPDX-License-Identifier: MIT -->

# Release check — 13 September 2026

| Plugin | Findings and action |
| --- | --- |
| Metafolder | GitHub source was 1.2.0, latest downloadable release 1.1.0. The installed linked checkout also contained unpublished folder-browser and optional-service boot fixes. These are included in 1.2.1. |
| Model Picker Augmented | Release 1.1.2 runtime files match the installed linked checkout byte for byte. Existing release retained. |
| Augmentor | Release 0.1.32 matched all 40 compared local extension, bridge, installer, shared and plugin files. Installed plugin runtime files matched the source. GitHub's default branch contains the compatibility changes. Existing release retained. |
| Adaptive Reasoning | GitHub and the installed package had matching 0.2.0 runtime source. Added public setup documentation and the first downloadable preview package; reasoning policy unchanged. |

## Checks performed

- Metafolder: regenerated browser bundle, syntax/export smoke check, folder
  navigation/hidden-file/fallback/error/cancellation regression suite, and
  packaged installation/composition/removal in a disposable DSH home.
- Model Picker: three API compatibility regression tests passed; downloaded
  release runtime files compared with the installed source.
- Adaptive Reasoning: 48 tests passed, actual DSH loop + adapter integration
  against a deterministic local endpoint passed, and packaged install,
  composition and removal passed in a disposable DSH home.
- Augmentor: existing published distribution downloaded and compared with the
  local checkout. No new browser automation or live-model test was run in this
  release audit; earlier compatibility evidence remains in its repository.
- New package contents reviewed; private session outputs, local deployment
  records, credentials and dependency trees are excluded.

These are disk/package checks. They do not prove that a long-running process or
an already-open browser tab has reloaded the latest files. No user service was
restarted and no model inference was requested for this audit. No idle GPU
warm-up, polling job or recurring release checker was added.

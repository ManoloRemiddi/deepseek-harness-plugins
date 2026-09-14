<!-- Copyright © 2026 Manolo Remiddi · SPDX-License-Identifier: MIT -->
# Collection update — 14 September 2026

Added Steering 0.1.0, tested on DSH 0.1.5-rc.1 with Node 24.19.0. The released package ran in an isolated agent preset without Augmentor’s built-in steering hook: correction delivery took 18 ms during model generation, the ordinary queued follow-up was preserved, and inputs were delivered once. Four regression tests cover cancellation races and tool boundaries. A separate live shell-command test confirmed steering waits for a running tool to finish.

The other five release assets are unchanged from the September 13 collection. The collection builder verifies all six SHA-256 hashes and the resulting ZIP. This does not assert compatibility with untested DSH versions or every plugin combination.

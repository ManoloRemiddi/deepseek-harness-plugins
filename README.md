<!-- Copyright © 2026 Manolo Remiddi · SPDX-License-Identifier: MIT -->

# DeepSeek Harness Plugins

Plugins by [Manolo Remiddi](https://github.com/ManoloRemiddi) for
[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).
Choose a plugin below, download its release and follow its installation guide.
Each plugin has its own repository, license, issues and version history.

## Choose a plugin

| Plugin | What it adds | Release | Get started |
| --- | --- | --- | --- |
| **[Metafolder](https://github.com/ManoloRemiddi/DSH-Metafolder-Plugin)** | Coloured sidebar groups for workspaces and sessions, plus folder browsing | **1.2.1** | [Download](https://github.com/ManoloRemiddi/DSH-Metafolder-Plugin/releases/tag/v1.2.1) · [Guide](https://github.com/ManoloRemiddi/DSH-Metafolder-Plugin#readme) |
| **[Model Picker Augmented](https://github.com/ManoloRemiddi/dsh-model-picker-augmented)** | Search, pin and hide models; refresh provider catalogues | **1.1.2** | [Download](https://github.com/ManoloRemiddi/dsh-model-picker-augmented/releases/tag/v1.1.2) · [Guide](https://github.com/ManoloRemiddi/dsh-model-picker-augmented#readme) |
| **[Augmentor](https://github.com/ManoloRemiddi/augmentor-dsh-extension-plugin)** | Chromium side panel and agent control of your real browser | **0.1.32** | [Download](https://github.com/ManoloRemiddi/augmentor-dsh-extension-plugin/releases/tag/v0.1.32) · [Guide](https://github.com/ManoloRemiddi/augmentor-dsh-extension-plugin#install) |
| **[Adaptive Reasoning](https://github.com/ManoloRemiddi/dsh-adaptive-reasoning)** | Automatically chooses effort for each request without a classifier model or GPU keep-alive | **0.2.0 preview** — model-specific configuration required | [Download](https://github.com/ManoloRemiddi/dsh-adaptive-reasoning/releases/tag/v0.2.0) · [Setup](https://github.com/ManoloRemiddi/dsh-adaptive-reasoning/blob/main/docs/SETUP.md) |

| **[Prompt Library](https://github.com/ManoloRemiddi/dsh-prompt-library)** | Save and edit reusable prompts, with standalone storage or an existing Augmentor service | **0.2.1 preview** | [Download](https://github.com/ManoloRemiddi/dsh-prompt-library/releases/tag/v0.2.1) · [Guide](https://github.com/ManoloRemiddi/dsh-prompt-library#readme) |

These versions were checked against **DSH 0.1.5-rc.1**. They are community
plugins, not official DeepSeek products. Other DSH versions may change plugin
interfaces. Augmentor's installation is verified on Linux with Chromium;
check each repository for its Node.js and profile requirements.

## Install

First install DSH and configure a working model. Use the complete local web URL
printed by DSH, including its authentication token, when opening the web app.

For a single-package plugin, download its `.tgz` release asset and run:

```sh
dsh plugin --profile web add /absolute/path/to/downloaded-plugin.tgz
```

Use the package asset under **Assets**, not GitHub's automatically generated
“Source code” archive. Use your actual DSH profile if different from `web`.
Finish running tasks, restart your existing DSH process and reload the web page.
An existing manual `link:` or symlink installation should be updated in place
following its guide, without adding a second copy.

**Augmentor** needs the complete distribution ZIP, browser extension and native
host installation; follow its guide rather than installing only the plugin.
**Prompt Library** needs Python 3 with SQLite for its standalone store; existing
Augmentor users can configure their shared service socket instead. Its default
standalone store starts empty without migrating or deleting previous data.
**Adaptive Reasoning** requires a one-time allowlist/effort configuration for
your own model; the stock package is inactive outside its tested route.

To remove a CLI-installed package:

```sh
dsh plugin --profile web remove PACKAGE_NAME
```

Restart DSH afterward. Augmentor's native host and browser extension have their
own removal steps. For manual installations, follow the repository's guide.

## Compatibility and release checks

[September 2026 release check](docs/RELEASE-CHECK-2026-09-13.md) records what was
compared and tested. Test results are not a promise of compatibility with every
model, browser or future DSH version. Adaptive Reasoning is explicitly a preview;
its fast paths are conservative English rules, not a trained difficulty judge.
Metafolder stores groups in browser localStorage; cross-device sync is not provided.

## Help and contributions

Open an issue in the affected plugin's repository. Include the plugin and DSH
versions, operating system/browser, install method, reproduction steps and the
error message. Use synthetic examples and remove credentials and private logs.
For a broken catalogue link, open an issue in this repository.

The repositories share the `deepseek-harness`, `dsh-plugin` and
`manolo-dsh-plugins` topics. You can also
[browse the collection by topic](https://github.com/search?q=user%3AManoloRemiddi+topic%3Amanolo-dsh-plugins&type=repositories).
Watch an individual repository's **Releases** for new versions. This catalogue
is updated when a release is published; it does not run a background updater.

MIT © 2026 Manolo Remiddi. See each plugin's license for its code.

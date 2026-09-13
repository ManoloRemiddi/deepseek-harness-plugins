<!-- Copyright © 2026 Manolo Remiddi · SPDX-License-Identifier: MIT -->
# Augmentor plugin collection — 13 September 2026

Five individually installable packages for DeepSeek Harness. This archive is a
convenient download, not an automatic installer. Choose only the plugins you want.
Two packages are previews and need the setup considerations described below.
The plugins were checked individually with DSH 0.1.5-rc.1; this collection does
not claim that every combination or future DSH version has been tested together.

## Before installing

Use a working DSH web profile and Node.js 22.19+ or 24+. These instructions target
Linux; Augmentor's browser integration was checked with Chromium. Preserve your
existing profile, settings, chats and linked package registrations. A new download
does not require deleting or overwriting your existing installation.

Extract this collection ZIP. The `packages` directory contains the original,
unmodified release downloads. Their individual licenses and documentation remain
inside them; `collection.json` records versions, sources and SHA-256 hashes.

## Install individual packages

For Metafolder and Model Picker, from the extracted collection directory:

```sh
dsh plugin --profile web add "$PWD/packages/dsh-metafolder-plugin-1.2.1.tgz"
dsh plugin --profile web add "$PWD/packages/dsh-model-picker-augmented-1.1.2.tgz"
```

Run only the command for the plugin you want. Existing manual symlink or `link:`
users should update their current checkout following its guide, without adding
a second bundle registration. Use your actual profile if different from `web`.

**Augmentor 0.1.32:** extract `packages/augmentor-0.1.32-dist.zip` to a permanent
directory. Keep its plugin, extension and native host together. Follow the
included README to load the unpacked Chromium extension, install the native
host using your extension ID, and install the DSH plugin. Installing only the
plugin does not complete browser integration.
[Full guide](https://github.com/ManoloRemiddi/augmentor-dsh-extension-plugin#install).

**Prompt Library 0.2.1 preview:** needs Python 3 with SQLite for its default
standalone store. It starts with an empty library and does not migrate or delete
older prompts. Existing Augmentor users can set `DSH_PROMPT_LIBRARY_SOCKET` in
DSH's environment to their already-running prompt service instead.

```sh
dsh plugin --profile web add "$PWD/packages/dsh-prompt-library-0.2.1.tgz"
```

[Storage and upgrade guide](https://github.com/ManoloRemiddi/dsh-prompt-library#readme).

**Adaptive Reasoning 0.2.0 preview:** the stock package only acts on its tested
Augmentor preset and Qwen route. On other installations, follow the setup guide
to create a package configured for your preset/provider/model and supported
effort values. It is inactive for unmatched routes. No GPU keep-alive is added.
For the exact tested route, the included package can be installed with:

```sh
dsh plugin --profile web add "$PWD/packages/dsh-adaptive-reasoning-0.2.0.tgz" --ignore-scripts --config.auto-install-peers=false
```

[One-time setup](https://github.com/ManoloRemiddi/dsh-adaptive-reasoning/blob/v0.2.0/docs/SETUP.md).

After installing your chosen plugins, finish active tasks, restart your existing
DSH process and reload the browser page. Open the complete local URL printed by
DSH if authentication is required. No new service instance is needed.

## Updates, verification and removal

This is a dated snapshot; future releases are listed at
https://augmentoragent.com/plugins.html and in each plugin's repository.
To verify the contents from the extracted directory on Linux:

```sh
sha256sum -c SHA256SUMS
```

To remove a CLI-installed plugin, use `dsh plugin --profile web remove PACKAGE_NAME`
and restart DSH. Augmentor's extension/native host have separate removal steps.
Prompt Library leaves its data intact; Metafolder leaves its browser groups intact.
Report issues to the relevant repository using synthetic examples, without
credentials or private session logs.

#!/usr/bin/env python3
# Copyright © 2026 Manolo Remiddi · SPDX-License-Identifier: MIT
"""Build a pinned download collection from verified upstream release assets."""
import hashlib
import json
from pathlib import Path
import urllib.request
import zipfile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'collection.json').read_text())
version = manifest['collection']
prefix = f'augmentor-plugins-{version}'
output = root / 'dist'
output.mkdir(exist_ok=True)
assets = {}
for plugin in manifest['plugins']:
    request = urllib.request.Request(plugin['url'], headers={'User-Agent': 'Augmentor-plugin-collection'})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    if hashlib.sha256(data).hexdigest() != plugin['sha256']:
        raise SystemExit(f"Checksum mismatch: {plugin['filename']}")
    assets['packages/' + plugin['filename']] = data

assets['GETTING-STARTED.md'] = (root / 'docs/COLLECTION-INSTALL.md').read_bytes()
assets['collection.json'] = (root / 'collection.json').read_bytes()
assets['LICENSE'] = (root / 'LICENSE').read_bytes()
assets['SHA256SUMS'] = ''.join(f'{hashlib.sha256(data).hexdigest()}  {name}\n' for name, data in sorted(assets.items())).encode()
archive = output / (prefix + '.zip')
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
    for name, data in sorted(assets.items()):
        entry = zipfile.ZipInfo(prefix + '/' + name, date_time=(2026, 9, 13, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        bundle.writestr(entry, data)
with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    for plugin in manifest['plugins']:
        data = bundle.read(prefix + '/packages/' + plugin['filename'])
        assert hashlib.sha256(data).hexdigest() == plugin['sha256']
(output / (prefix + '-SHA256SUMS')).write_text(hashlib.sha256(archive.read_bytes()).hexdigest() + '  ' + archive.name + '\n')
print(f'Verified {len(manifest["plugins"])} pinned packages; built {archive} ({archive.stat().st_size:,} bytes).')

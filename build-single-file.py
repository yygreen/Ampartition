#!/usr/bin/env python3
"""Inline every images/ reference back into index.html as base64.

Produces proposal-single-file.html: one self-contained file you can email,
attach or print with no folder around it. The live site does not need this;
it is only for handing the proposal to someone as a single attachment.

    python3 build-single-file.py
"""
import base64, mimetypes, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
src = ROOT / "index.html"
out = ROOT / "proposal-single-file.html"

html = src.read_text(encoding="utf-8")
missing = []

def inline(m):
    rel = m.group(1)
    path = ROOT / rel
    if not path.exists():
        missing.append(rel)
        return m.group(0)
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'src="data:{mime};base64,{b64}"'

html = re.sub(r'src="(images/[^"]+)"', inline, html)

if missing:
    sys.exit("missing image files: " + ", ".join(missing))

out.write_text(html, encoding="utf-8")
print(f"wrote {out.name} ({out.stat().st_size:,} bytes)")

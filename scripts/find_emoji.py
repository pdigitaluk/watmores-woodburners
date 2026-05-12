"""Find all non-ASCII characters in HTML files."""
import os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

emoji_re = re.compile(r'[\U00010000-\U0010ffff☀-⟿⬀-⯿︀-️]')

found = {}
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('scripts', '.git', 'node_modules')]
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        with open(path, encoding='utf-8') as fh:
            for line in fh:
                for m in emoji_re.finditer(line):
                    ch = m.group()
                    rel = os.path.relpath(path, BASE)
                    if ch not in found:
                        found[ch] = set()
                    found[ch].add(rel)

for ch in sorted(found.keys(), key=lambda c: ord(c)):
    line = f'{repr(ch):20s}  U+{ord(ch):04X}  ->  {", ".join(sorted(found[ch])[:4])}'
    print(line.encode('ascii', errors='replace').decode('ascii'))

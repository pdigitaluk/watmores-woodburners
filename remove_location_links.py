import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# Match from the opening <div> of the Chimney Sweeping column through
# to the closing </div> of the Woodburner Installation column,
# stopping just before <hr class="footer-divider">
PATTERN = re.compile(
    r'\s*<div>\s*<div class="f-heading">Chimney Sweeping</div>.*?</div>\s*<div>\s*<div class="f-heading">Woodburner Installation</div>.*?</div>',
    re.DOTALL
)

pages = []
root_html = os.path.join(BASE, 'index.html')
if os.path.exists(root_html):
    pages.append(root_html)
for d in os.listdir(BASE):
    p = os.path.join(BASE, d, 'index.html')
    if os.path.isfile(p):
        pages.append(p)

updated = 0
for path in pages:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'f-heading">Chimney Sweeping' not in html:
        continue
    new_html = PATTERN.sub('', html)
    if new_html == html:
        print(f"NO MATCH: {os.path.relpath(path, BASE)}")
        continue
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    updated += 1
    print(f"CLEANED: {os.path.relpath(path, BASE)}")

print(f"\nDone. {updated} pages cleaned.")

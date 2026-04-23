import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

START = '      <div>\n        <div class="f-heading">Chimney Sweeping</div>'
END   = '      </div>\n    <hr class="footer-divider">'
CLEAN = '    <hr class="footer-divider">'

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
    if START not in html:
        continue
    # Remove everything from START up to and including the closing </div> before the hr
    new_html = re.sub(
        r'      <div>\s*<div class="f-heading">Chimney Sweeping</div>.*?</div>\s*</div>\s*<hr class="footer-divider">',
        '    <hr class="footer-divider">',
        html, flags=re.DOTALL
    )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    updated += 1
    print(f"CLEANED: {os.path.relpath(path, BASE)}")

print(f"\nDone. {updated} pages cleaned.")

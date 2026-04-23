"""
Injects a location links section into the footer of every HTML page.
The block goes just before <hr class="footer-divider"> in the footer.
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

LOCATION_BLOCK = """      <div>
        <div class="f-heading">Chimney Sweeping</div>
        <ul>
          <li><a href="/chimney-sweep-norwich/">Chimney Sweep Norwich</a></li>
          <li><a href="/chimney-sweep-aylsham/">Chimney Sweep Aylsham</a></li>
          <li><a href="/chimney-sweep-cromer/">Chimney Sweep Cromer</a></li>
          <li><a href="/chimney-sweep-fakenham/">Chimney Sweep Fakenham</a></li>
          <li><a href="/chimney-sweep-north-walsham/">Chimney Sweep North Walsham</a></li>
          <li><a href="/chimney-sweep-holt/">Chimney Sweep Holt</a></li>
          <li><a href="/chimney-sweep-sheringham/">Chimney Sweep Sheringham</a></li>
          <li><a href="/chimney-sweep-wroxham/">Chimney Sweep Wroxham</a></li>
          <li><a href="/chimney-sweep-dereham/">Chimney Sweep Dereham</a></li>
          <li><a href="/chimney-sweep-wymondham/">Chimney Sweep Wymondham</a></li>
          <li><a href="/chimney-sweep-attleborough/">Chimney Sweep Attleborough</a></li>
          <li><a href="/chimney-sweep-great-yarmouth/">Chimney Sweep Great Yarmouth</a></li>
          <li><a href="/chimney-sweep-kings-lynn/">Chimney Sweep King's Lynn</a></li>
        </ul>
      </div>
      <div>
        <div class="f-heading">Woodburner Installation</div>
        <ul>
          <li><a href="/woodburner-installer-norwich/">Woodburner Installer Norwich</a></li>
          <li><a href="/woodburner-installer-aylsham/">Woodburner Installer Aylsham</a></li>
          <li><a href="/woodburner-installer-cromer/">Woodburner Installer Cromer</a></li>
          <li><a href="/woodburner-installer-fakenham/">Woodburner Installer Fakenham</a></li>
          <li><a href="/woodburner-installer-north-walsham/">Woodburner Installer North Walsham</a></li>
          <li><a href="/woodburner-installer-holt/">Woodburner Installer Holt</a></li>
          <li><a href="/woodburner-installer-sheringham/">Woodburner Installer Sheringham</a></li>
          <li><a href="/woodburner-installer-wroxham/">Woodburner Installer Wroxham</a></li>
          <li><a href="/woodburner-installer-dereham/">Woodburner Installer Dereham</a></li>
          <li><a href="/woodburner-installer-wymondham/">Woodburner Installer Wymondham</a></li>
          <li><a href="/woodburner-installer-attleborough/">Woodburner Installer Attleborough</a></li>
          <li><a href="/woodburner-installer-great-yarmouth/">Woodburner Installer Great Yarmouth</a></li>
          <li><a href="/woodburner-installer-kings-lynn/">Woodburner Installer King's Lynn</a></li>
        </ul>
      </div>
"""

MARKER = '    <hr class="footer-divider">'

pages = []
# Root index.html
root_html = os.path.join(BASE, 'index.html')
if os.path.exists(root_html):
    pages.append(root_html)
# All subdirectory index.html files
for d in os.listdir(BASE):
    p = os.path.join(BASE, d, 'index.html')
    if os.path.isfile(p):
        pages.append(p)

updated = 0
skipped = 0
for path in pages:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    if LOCATION_BLOCK.strip()[:40] in html:
        skipped += 1
        continue
    if MARKER not in html:
        print(f"NO MARKER: {path}")
        continue
    new_html = html.replace(MARKER, LOCATION_BLOCK + MARKER, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    updated += 1
    name = os.path.relpath(path, BASE)
    print(f"UPDATED: {name}")

print(f"\nDone. {updated} updated, {skipped} already had links.")

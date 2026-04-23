import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

SECTIONS = {

  # ── CHIMNEY SWEEP PAGES ───────────────────────────────────────────────────

  "chimney-sweep-cromer": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Cromer</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian and Edwardian seaside terraces</h3>
        <p>Cromer was developed heavily between 1880 and 1910, and the town centre has a dense concentration of period terraces and seafront villas with original chimney stacks — often with multiple pots serving different rooms on the same stack.</p>
      </div>
      <div class="three-col-item">
        <h3>Flint cottages and coastal properties</h3>
        <p>The area's traditional flint construction is beautiful but the salt air from the North Sea accelerates mortar erosion around chimney pots and flashings. We flag any deterioration we find during the sweep.</p>
      </div>
      <div class="three-col-item">
        <h3>Holiday lets and second homes</h3>
        <p>Cromer has a high density of holiday properties that can sit unheated and unused for months at a time. We recommend a pre-season sweep and inspection before guests arrive — and issue a certificate on every visit.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-fakenham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Fakenham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian and Edwardian town houses</h3>
        <p>Fakenham's town centre has a good spread of period terraced and semi-detached properties with original chimney breasts. Many have had insert fireplaces removed over the years — we can advise on whether they're ready for a new stove.</p>
      </div>
      <div class="three-col-item">
        <h3>Norfolk flint farmhouses and cottages</h3>
        <p>The villages around Fakenham are full of working farms and traditional flint cottages — many with Aga and Rayburn range flues as well as open hearth fireplaces. We sweep all types and cover the full area regularly.</p>
      </div>
      <div class="three-col-item">
        <h3>Wells and north Norfolk coast villages</h3>
        <p>The road north from Fakenham towards Wells-next-the-Sea passes through some of Norfolk's most characterful brick and flint villages — all within our regular sweep run and usually bookable within the week.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-north-walsham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>North Walsham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Georgian and Victorian town centre</h3>
        <p>North Walsham's market town core includes some elegant period properties with large multi-flue chimney systems. Original clay liners in these properties can be fragile and benefit from careful annual cleaning.</p>
      </div>
      <div class="three-col-item">
        <h3>Post-war semis and bungalows</h3>
        <p>Much of North Walsham's housing stock dates from the 1950s–1970s, built with solid fuel fireplaces as standard. Many were converted to gas and then back again — these transitional flues often need a thorough clean after years of mixed use.</p>
      </div>
      <div class="three-col-item">
        <h3>Coastal villages and surrounding area</h3>
        <p>Mundesley, Happisburgh, Walcott and the Poppyland coast villages are all within our regular North Walsham run — usually combined on the same day to give quick availability across the whole area.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-wroxham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Wroxham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Riverside Broads cottages</h3>
        <p>Properties along the Bure and the Broadland waterways are often holiday lets with period flues that can go unused for months at a time. We recommend an annual inspection — damp conditions in unheated properties can lead to liner deterioration.</p>
      </div>
      <div class="three-col-item">
        <h3>Holiday and second home properties</h3>
        <p>The Broads area has a high density of second homes and short-term let properties. We sweep before the season starts and issue a certificate that satisfies both the insurer and the letting agent's compliance requirements.</p>
      </div>
      <div class="three-col-item">
        <h3>Coltishall and Horstead village properties</h3>
        <p>The Bure valley villages flanking Wroxham have a high concentration of traditional Norfolk brick properties with original flue systems. We cover these regularly on our Broadland run and are usually available within the week.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-holt": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Holt</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Georgian market town properties</h3>
        <p>Holt is one of Norfolk's most elegant small towns, rebuilt largely in Georgian style after the fire of 1708. Many of these properties have substantial original chimney systems that are still in active daily use and benefit from careful annual sweeping.</p>
      </div>
      <div class="three-col-item">
        <h3>Country estate and rural houses</h3>
        <p>The land around Holt includes some of north Norfolk's finest rural properties. We regularly sweep at Letheringsett, Edgefield, Baconsthorpe, Thornage and the surrounding villages — all within our regular Holt service run.</p>
      </div>
      <div class="three-col-item">
        <h3>Flint cottages and barn conversions</h3>
        <p>The north Norfolk hinterland around Holt has a high density of converted agricultural buildings and traditional flint cottages, many with multiple flue systems. We sweep all types and advise clearly on condition.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-sheringham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Sheringham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian and Edwardian seafront terraces</h3>
        <p>Sheringham was developed primarily in the late Victorian and Edwardian eras. The town centre has a dense concentration of terraced properties with period chimney stacks — many still with original clay liners that require careful, thorough sweeping.</p>
      </div>
      <div class="three-col-item">
        <h3>Flint cottages in the old town</h3>
        <p>The older core of Sheringham has some classic north Norfolk flint and brick properties with original clay pot and brick flue systems. Salt air from the sea means mortar and pointing around pots can deteriorate faster than inland — we flag anything that needs attention.</p>
      </div>
      <div class="three-col-item">
        <h3>Upper Sheringham and surrounding villages</h3>
        <p>The area above the town — Beeston Regis, West Runton, Weybourne and the inland villages — are all within our regular Sheringham sweep run. We're usually in the area at least once a week.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-attleborough": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Attleborough</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian and Edwardian town centre</h3>
        <p>Attleborough's market town core has a solid stock of Victorian and Edwardian semi-detached and terraced properties with original chimney systems. We sweep the full flue and inspect the liner on every visit.</p>
      </div>
      <div class="three-col-item">
        <h3>Rural south Norfolk farmhouses</h3>
        <p>The villages surrounding Attleborough — Old Buckenham, New Buckenham, Kenninghall, Rockland All Saints — have a high proportion of agricultural properties with Aga, Rayburn and open hearth flues. We sweep all types.</p>
      </div>
      <div class="three-col-item">
        <h3>Post-war and newer estates</h3>
        <p>The more recent housing around Attleborough includes properties where fireplaces were fitted as standard and later blocked. Many homeowners are re-opening these for wood burners — we can advise on condition and sweep ahead of installation.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-wymondham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Wymondham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Historic market town centre</h3>
        <p>Wymondham has one of Norfolk's finest market places, surrounded by a mix of medieval, Georgian and Victorian properties with substantial original chimney systems. We're familiar with the town's older stock and sweep here regularly.</p>
      </div>
      <div class="three-col-item">
        <h3>Victorian and Edwardian terraces</h3>
        <p>The residential streets around the town centre have a good spread of period terraced properties with single and double chimney stacks. Many have been converted to wood burners and require annual sweeping to keep insurance valid.</p>
      </div>
      <div class="three-col-item">
        <h3>South Norfolk villages</h3>
        <p>Hethersett, Hethel, Wreningham, Ketteringham and the surrounding villages are within our regular Wymondham service run — all usually available within the week with a certificate issued on every visit.</p>
      </div>
    </div>
  </div>
</section>
""",

  "chimney-sweep-aylsham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Properties We Sweep in <strong>Aylsham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Georgian and Victorian market town properties</h3>
        <p>Aylsham's market place is surrounded by Georgian and Victorian properties with substantial original chimney systems. Many are still in daily use and benefit from careful annual cleaning by a registered sweep.</p>
      </div>
      <div class="three-col-item">
        <h3>Blickling Estate and rural cottages</h3>
        <p>The villages around Aylsham — particularly those close to the Blickling Estate — have a high concentration of traditional Norfolk brick and flint cottages, many with period flue systems that we sweep on a regular annual basis.</p>
      </div>
      <div class="three-col-item">
        <h3>Bure Valley farmhouses and conversions</h3>
        <p>The Bure Valley east of Aylsham has a range of agricultural and converted properties — from working farmhouses with Aga flues to barn conversions with newer stove installations. We cover the full area on our regular north Norfolk run.</p>
      </div>
    </div>
  </div>
</section>
""",

  # ── WOODBURNER INSTALLER PAGES ────────────────────────────────────────────

  "woodburner-installer-cromer": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Cromer</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian and Edwardian seaside properties</h3>
        <p>Cromer's substantial period housing stock frequently has original chimney breasts with blocked or removed inserts — ideal for a new stove with a fresh stainless steel liner. We survey and advise on every property before quoting.</p>
      </div>
      <div class="three-col-item">
        <h3>Holiday lets and coastal rentals</h3>
        <p>A wood burner is one of the most effective ways to increase occupancy and nightly rate for a Cromer holiday let. We install in short-term let properties regularly and can advise on the right stove output for the space.</p>
      </div>
      <div class="three-col-item">
        <h3>Flint cottages and rural north Norfolk</h3>
        <p>The villages behind Cromer — Northrepps, Roughton, Sustead, Aldborough — have some of Norfolk's most characterful flint properties. Where there's no existing chimney we install twin-wall flue systems as a complete solution.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-fakenham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Fakenham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Farmhouses and agricultural properties</h3>
        <p>The villages around Fakenham have a high proportion of working farms and rural houses where we install larger-output stoves as primary or supplementary heating. Off-grid properties are a particular strength — no gas connection needed.</p>
      </div>
      <div class="three-col-item">
        <h3>Traditional flint and brick cottages</h3>
        <p>North Norfolk's distinctive building style creates chimney systems that need careful re-lining before installation. We carry out all liner work as part of every job — no subcontractors, no additional charges.</p>
      </div>
      <div class="three-col-item">
        <h3>Market town semis and terraces</h3>
        <p>Fakenham's Victorian and inter-war residential streets have a solid stock of chimney breasts ready for installation. We survey the whole property, confirm which flues are usable and give a fixed price before we start.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-north-walsham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>North Walsham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian terraces with original chimney breasts</h3>
        <p>North Walsham's town centre terraces frequently have chimney breasts in multiple rooms. We survey the whole property, confirm which flue is best suited, and give a fixed price before any work begins.</p>
      </div>
      <div class="three-col-item">
        <h3>Post-war housing with blocked fireplaces</h3>
        <p>A large proportion of North Walsham's 1950s–1970s housing stock has fireplaces that were blocked when central heating arrived. Reopening and lining these for a new stove is often more straightforward than people expect.</p>
      </div>
      <div class="three-col-item">
        <h3>Rural Broadland and coast villages</h3>
        <p>Stalham, Happisburgh, Mundesley and the villages east and south of North Walsham are all within our regular installation area — usually combined on the same run to give fast availability.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-wroxham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Wroxham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Norfolk Broads properties and riverside homes</h3>
        <p>We've installed in riverside cottages, boatyards and holiday properties throughout the Broads area. Waterside properties often have damp conditions that benefit particularly from a stove that dries the air and reduces condensation.</p>
      </div>
      <div class="three-col-item">
        <h3>Holiday let properties in Wroxham and Hoveton</h3>
        <p>A wood burner is one of the most reliable ways to increase occupancy rates in a Broads holiday let. We regularly install in properties managed by Broadland letting agents and can turn round most jobs quickly.</p>
      </div>
      <div class="three-col-item">
        <h3>Coltishall and Horstead village properties</h3>
        <p>The Bure valley villages have a mix of traditional brick-built and flint properties, many with original chimney stacks well-suited to stove installation. We cover the full area on our regular Broadland run.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-holt": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Holt</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Georgian and listed town centre properties</h3>
        <p>Holt's Georgian core includes some of Norfolk's finest period properties. Listed building installations require careful handling of existing flue systems — we are experienced in working within listed building constraints and advise clearly before starting.</p>
      </div>
      <div class="three-col-item">
        <h3>Country estate and large rural houses</h3>
        <p>The area around Holt includes some notable rural properties with larger rooms that benefit from higher-output stoves. We advise on the right stove output for every room during the free survey — no guesswork.</p>
      </div>
      <div class="three-col-item">
        <h3>Flint and brick village properties</h3>
        <p>Letheringsett, Baconsthorpe, Thornage, Edgefield and the surrounding north Norfolk villages all have traditional properties where we install on a regular basis. Twin-wall flue systems are available where there's no existing chimney stack.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-sheringham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Sheringham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian and Edwardian seaside terraces</h3>
        <p>Sheringham's predominantly Victorian housing stock has a high proportion of properties with original chimney stacks in good condition. Many already have a liner in place and simply need a stove selecting and fitting — we advise on the right model for every room.</p>
      </div>
      <div class="three-col-item">
        <h3>Flint cottages and upper town properties</h3>
        <p>The older parts of Sheringham and the surrounding villages have traditional flint properties with clay pot flue systems. We re-line these as part of every installation — the new liner is included in the quoted price.</p>
      </div>
      <div class="three-col-item">
        <h3>Beeston Regis and west Norfolk villages</h3>
        <p>The villages immediately west of Sheringham — Beeston Regis, West Runton, Weybourne and beyond — are all within our regular installation area. We cover the full north Norfolk coast on a regular run.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-attleborough": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Attleborough</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Victorian and Edwardian town centre properties</h3>
        <p>Properties around Attleborough's market place and the surrounding streets frequently have chimney breasts in excellent condition — ideal for installation. We survey and confirm the flue is ready before quoting a fixed price.</p>
      </div>
      <div class="three-col-item">
        <h3>South Norfolk farmhouses and barn conversions</h3>
        <p>The villages south of Attleborough towards Thetford and the Suffolk border have a high proportion of agricultural properties. We regularly install in barn conversions and working farmhouses in this area, including off-grid properties with no gas supply.</p>
      </div>
      <div class="three-col-item">
        <h3>Post-war and modern properties</h3>
        <p>An increasing number of our Attleborough installations are in properties without an existing chimney stack. We install twin-wall flue systems through the roof as a complete self-contained solution — no chimney required.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-wymondham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Wymondham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Historic town centre and period properties</h3>
        <p>Wymondham has a rich stock of Georgian and Victorian properties with original chimney systems well-suited to wood burner installation. We survey every property before quoting and advise honestly on whether the existing flue can be used.</p>
      </div>
      <div class="three-col-item">
        <h3>Victorian and Edwardian terraces</h3>
        <p>The residential streets around the town centre have solid chimney breasts in good condition. We install in these regularly — fitting a new stainless steel liner and a modern efficient stove, usually completed in a single day.</p>
      </div>
      <div class="three-col-item">
        <h3>South Norfolk villages</h3>
        <p>Hethersett, Hethel, Wreningham, Mulbarton and the surrounding villages south of Norwich are all within our regular installation run. We cover this area on a weekly basis and can usually book within a fortnight.</p>
      </div>
    </div>
  </div>
</section>
""",

  "woodburner-installer-aylsham": """
<section class="sec sec-off">
  <div class="sec-inner">
    <div class="eyebrow">Local property types</div>
    <h2 class="sec-title">Installations We Carry Out in <strong>Aylsham</strong></h2>
    <div class="three-col-grid">
      <div class="three-col-item">
        <h3>Georgian and Victorian market town properties</h3>
        <p>Aylsham's market town centre has a good spread of period properties with original chimney breasts. We survey each one individually — confirming the flue condition, measuring the room and advising on the right stove output before quoting.</p>
      </div>
      <div class="three-col-item">
        <h3>Blickling Estate and rural cottages</h3>
        <p>The villages around Aylsham — particularly those close to the Blickling Estate — have a high concentration of traditional Norfolk flint and brick cottages. We install regularly in this area, including properties that require a full liner replacement.</p>
      </div>
      <div class="three-col-item">
        <h3>Bure Valley farmhouses and barn conversions</h3>
        <p>The agricultural properties east of Aylsham along the Bure Valley are well-suited to larger-output stoves. Barn conversions without an existing chimney are solved with a twin-wall flue system — everything included in a single fixed price.</p>
      </div>
    </div>
  </div>
</section>
""",
}

MARKER = '<section class="sec sec-black">'

for folder, html in SECTIONS.items():
    path = os.path.join(BASE, folder, "index.html")
    if not os.path.exists(path):
        print(f"SKIP (not found): {folder}")
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "three-col-grid" in content:
        print(f"SKIP (already has section): {folder}")
        continue
    # Insert before first occurrence of the marker
    idx = content.find(MARKER)
    if idx == -1:
        print(f"SKIP (marker not found): {folder}")
        continue
    new_content = content[:idx] + html + content[idx:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"UPDATED: {folder}")

print("Done.")

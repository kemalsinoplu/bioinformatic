## 28. makaleden KEGG chapterini okudum . Oradan KEGG sitesine gittim ve makalede viral bozukluklar hakkında
# bilgi verilmişti bende bu yüzden viral genomların datasetini indirdim. dataset xml şekilde idi
# bu yüzden aşağıdaki gibi parse ettim.


import xml.etree.ElementTree as ET

# XML dosyasını açtım:
with open("ko03230.xml", "r", encoding="utf-8") as file:
    xml_data = file.read()

# XML verisini parse ettim:
root = ET.fromstring(xml_data)

# Patika bilgilerini aldım:
pathway_name = root.attrib.get('name')
organism = root.attrib.get('org')
pathway_number = root.attrib.get('number')
title = root.attrib.get('title')
image = root.attrib.get('image')
link = root.attrib.get('link')

print(f"Pathway Name: {pathway_name}")
print(f"Organism: {organism}")
print(f"Pathway Number: {pathway_number}")
print(f"Title: {title}")
print(f"Image: {image}")
print(f"Link: {link}")

# Entry bilgilerini aldım:
entries = root.findall('.//entry')
for entry in entries:
    entry_id = entry.attrib.get('id')
    entry_name = entry.attrib.get('name')
    entry_type = entry.attrib.get('type')
    entry_link = entry.attrib.get('link')

    graphics = entry.find('graphics')
    graphics_name = graphics.attrib.get('name')
    graphics_fgcolor = graphics.attrib.get('fgcolor')
    graphics_bgcolor = graphics.attrib.get('bgcolor')
    graphics_type = graphics.attrib.get('type')
    graphics_x = graphics.attrib.get('x')
    graphics_y = graphics.attrib.get('y')
    graphics_width = graphics.attrib.get('width')
    graphics_height = graphics.attrib.get('height')

    print(f"\nEntry ID: {entry_id}")
    print(f"Entry Name: {entry_name}")
    print(f"Entry Type: {entry_type}")
    print(f"Entry Link: {entry_link}")
    print(f"Graphics Name: {graphics_name}")
    print(f"Graphics FGColor: {graphics_fgcolor}")
    print(f"Graphics BGColor: {graphics_bgcolor}")
    print(f"Graphics Type: {graphics_type}")
    print(f"Graphics X: {graphics_x}")
    print(f"Graphics Y: {graphics_y}")
    print(f"Graphics Width: {graphics_width}")
    print(f"Graphics Height: {graphics_height}")

import xml.etree.ElementTree as ET

# XML dosyasının adını belirtin
xml_file_path = "ReconMap-2.01-SBML3-Layout-Render.xml"

# XML dosyasını parse et
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Model bilgilerini al
model_id = root.find(".//{http://www.sbml.org/sbml/level3/version1/core}model").get("id")

# Renk tanımlamalarını ve stilleri al
colors = {}
styles = {}

for color_def in root.findall(".//{http://www.sbml.org/sbml/level3/version1/render/version1}colorDefinition"):
    color_id = color_def.get("render:id")
    color_value = color_def.get("render:value")
    colors[color_id] = color_value

for style in root.findall(".//{http://www.sbml.org/sbml/level3/version1/render/version1}style"):
    style_id = style.get("id")
    style_color_id = style.find(".//{http://www.sbml.org/sbml/level3/version1/render/version1}g").get("render:fill")
    styles[style_id] = colors[style_color_id]

# Layout bilgilerini al
layout_width = root.find(".//{http://www.sbml.org/sbml/level3/version1/layout/version1}dimensions").get("layout:width")
layout_height = root.find(".//{http://www.sbml.org/sbml/level3/version1/layout/version1}dimensions").get("layout:height")

print(f"Model ID: {model_id}")
print("Renk Tanımlamaları:")
print(colors)
print("Stil Tanımlamaları:")
print(styles)
print(f"Layout Bilgileri: Genişlik {layout_width}, Yükseklik {layout_height}")

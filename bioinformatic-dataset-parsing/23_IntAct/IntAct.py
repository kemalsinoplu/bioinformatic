import xml.etree.ElementTree as ET

xml_file_path = "covid.xml"

tree = ET.parse(xml_file_path)
root = tree.getroot()

short_label = root.find('.//shortLabel').text
full_name = root.find('.//fullName').text
interactor_type = root.find('.//interactorType/shortLabel').text
sequence = root.find('.//sequence').text

short_label = short_label_elem.text if short_label_elem is not None else None
full_name = full_name_elem.text if full_name_elem is not None else None
interactor_type = interactor_type_elem.text if interactor_type_elem is not None else None
sequence = sequence_elem.text if sequence_elem is not None else None

print(f"Short Label: {short_label}")
print(f"Full Name: {full_name}")
print(f"Interactor Type: {interactor_type}")
print(f"Sequence: {sequence}")
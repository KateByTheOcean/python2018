import xml.etree.ElementTree as ET
tree = ET.parse('VDA mix 2247.xml')
root = tree.getroot()

for child in root:
    print child.tag, child.attrib

for measurement in root.findall('measurements'):
    ftPressure = measurement.get('expected FlowTubePressure')
    print ftPressure

for method in root:
    print method.getchildren()
    

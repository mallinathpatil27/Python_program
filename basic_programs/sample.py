
import xml.etree.ElementTree as ET
 
# We're at the root node (<page>)
root_node = ET.parse('D:/pandas/sample.xml').getroot()
 
# We need to go one level below to get <items>
# and then one more level from that to go to <item>
for tag in root_node.findall('items/item'):
    # Get the value from the attribute 'name'
    value = tag.attrib['name']
    print(value)
    # Get the text of that tag
    print(tag.text)

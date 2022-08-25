import xml.etree.ElementTree as ET
df =ET.parse("D:/pandas/emp.xml")

root=df.getroot()
print(root.tag)
print(root.attrib)
treeOne = ET.fromstring(df)
print (treeOne.find('./neighbor').attrib['name'])
myroot=df.find('country')


for child in root[0]:
    print(child.tag,"-->",child.text,child.attrib)
    
print('------------------------')    

for child in root[1]:
    print(child.tag,"-->",child.text,child.attrib)
    
print('------------------------')

for child in root[2]:
    print(child.tag,"-->",child.text,child.attrib)






'''

for child in root:
    print(child.tag)


for child in root:
    print(child.tag,child.attrib)
'''
'''
for child in root.findall('country'):
    name=child.get('name')
    print(name)

    rank=child.find('rank').text
    print('rank',rank)

    year=child.find('year').text
    print('year',year)

    gdpc=child.find('gdppc').text
    print(gdpc)

    name1=child.find('neighbor name')
    print(name1)

    
'''
'''
    
print(root[0][3].text)
    
    


'''    

'''for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)'''

 
'''for country in root.findall('country'):
    rank=country.find('rank').text
    name=country.get('name')
    year=country.find('year').text
    gdpc=country.find('gdppc').text
    print(name,'-->',rank,year,gdpc) '''



    



    

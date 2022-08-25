import xml.etree.ElementTree as ET
import pandas as pd
df =ET.parse("D:/pandas/emp.xml")
root=df.getroot()

details1=[]
details2=[]
country_dtails=[]
neighbour_details=[]

for child in root.iter('country'):
    rank=child.find('rank').text
    year=child.find('year').text
    country_name=child.get('name')
    gdppc=child.find('gdppc').text
   # print(rank,year,country_name,gdppc)

    details1=[country_name,rank,year,gdppc]
    country_dtails.append(details1)
    
for i in root.findall('country/neighbor'):
    neigbour_name=i.get('name')
    direction=i.get('direction')
    #print(neigbour_name,direction)

    details2=[neigbour_name,direction]
    neighbour_details.append(details2)
    
list1=pd.DataFrame(country_dtails,columns=['country','rank','year','gdpc'])
list2=pd.DataFrame(neighbour_details,columns=['neigbour','direction'])


#print(list1.to_string(index=False)) 
#print(list2.to_string(index=False))
     
Final_list=pd.concat([list1,list2],axis=1)
print(Final_list)















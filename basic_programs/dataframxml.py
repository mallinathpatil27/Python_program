import xml.etree.ElementTree as ETree
import pandas as pd

# give the path where you saved the xml file
# inside the quotes
prstree = ETree.parse("D:/pandas/DF.xml")
root = prstree.getroot()

# print(root)
store_items = []
all_items = []

for storeno in root.iter('store'):
	
	store_Nr = storeno.attrib.get('slNo')
	itemsF = storeno.find('foodItem').text
	price = storeno.find('price').text
	quan = storeno.find('quantity').text
	dis = storeno.find('discount').text

	store_items = [store_Nr, itemsF, price, quan, dis]
	all_items.append(store_items)

xmlToDf = pd.DataFrame(all_items, columns=[
'SL No', 'ITEM_NUMBER', 'PRICE', 'QUANTITY', 'DISCOUNT'])

print(xmlToDf.to_string(index=False))

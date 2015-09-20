from db.models.item import Item

import xml.etree.ElementTree as ET
import copy

items = {}

def load_item_data():
	tree = ET.parse('../DB/itemDB.xml')
	root = tree.getroot()
	lista = root.getchildren()

	for itemXML in lista:
		item = Item()
		fields = itemXML.getchildren()
		item.set_values(fields)
		items[item.id] = item
	
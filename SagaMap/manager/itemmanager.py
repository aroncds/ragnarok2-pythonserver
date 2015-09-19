import xml.etree.ElementTree as ET
import copy

items = {}

class Item(object):
	id = None
	mesh = None
	icon = 0
	addition = 0
	questitem = 0
	equip_type = 0
	type = 0
	price = 0
	unknow1 = 0
	trade = 0
	drop = 0
	unknow3 = 0
	unknow4 = 0
	name = ""
	desc = ""
	quest = 0
	req_clv = 0
	req_male = 0
	req_female = 0
	req_norman = 0
	req_ellr = 0
	req_dimago = 0
	req_str = 0
	req_dex = 0
	req_int = 0
	req_con = 0
	req_luc = 0
	JobRequirement = []
	WeaponRequirement = []
	req_summons = 0
	req_addition = 0
	max_stack = 0
	max_dur = 0
	unknow2 = 0
	skill_id = 0
	option_id = 0

	def __init__(self):
		pass

	def serialize(packet, item, index):
		packet.setInt(index, item.id)
		packet.setUInt(index+4, 0)
		packet.setString(item.creatorName, index+8, 32)
		packet.setUInt(index + 45, 0)
		packet.data[index+46] = item.tradeAble
		packet.setUShort(index+47, item.durability)
		packet.setUInt(index+49, item.addition1)
		packet.setUInt(index+51, item.addition2)
		packet.setUInt(index+53, item.addition3)
		packet.data[55] = item.index
		packet.setUInt(index+54, item.Enchantments[0])
		packet.setUInt(index+58, item.Enchantments[1])
		packet.data[index+48] = item.Dye

	def clone(self):
		return copy.copy(self)


def load_item_data():
	tree = ET.parse('../DB/itemDB.xml')
	root = tree.getroot()
	lista = root.getchildren()
	length = len(lista)

	for itemXML in lista:
		item = Item()
		fields = itemXML.getchildren()
		
		for field in fields:
			if hasattr(item, field.tag):
				setattr(item, field.tag, field.text)
		
		items[item.id] = item
	
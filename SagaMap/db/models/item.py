from db import model


class Item(model.ModelXML):
	id = model.IntField()
	mesh = model.IntField()
	icon = model.IntField()
	addition = model.IntField()
	questitem = model.IntField()
	equip_type = model.IntField()
	type = model.IntField()
	price = model.IntField()
	unknow1 = model.IntField()
	trade = model.IntField()
	drop = model.IntField()
	unknow3 = model.IntField()
	unknow4 = model.IntField()
	name = model.CharField()
	desc = model.CharField()
	quest = model.IntField()
	req_clv = model.IntField()
	req_male = model.IntField()
	req_female = model.IntField()
	req_norman = model.IntField()
	req_ellr = model.IntField()
	req_dimago = model.IntField()
	req_str = model.IntField()
	req_dex = model.IntField()
	req_int = model.IntField()
	req_con = model.IntField()
	req_luc = model.IntField()
	JobRequirement = model.ListIntField()
	WeaponRequirement = model.ListIntField()
	req_summons = model.IntField()
	req_addition = model.IntField()
	max_stack = model.IntField()
	max_dur = model.IntField()
	unknow2 = model.IntField()
	skill_id = model.IntField()
	option_id = model.IntField()
	tradeAble = 0
	addition1 = 0
	addition2 = 0
	addition3 = 0
	enchantments = [0] * 2
	index = 0
	dye = 0

	def serialize(packet, inv, index):
		item = inv.item
		packet.setInt(index, item.id)
		packet.setUInt(index+4, 0)
		packet.setString(inv.creatorName, index+8, 32)
		packet.setUInt(index + 45, 0)
		packet.data[index+46] = item.tradeAble
		packet.setUShort(index+47, inv.durability)
		packet.setUInt(index+49, item.addition1)
		packet.setUInt(index+51, item.addition2)
		packet.setUInt(index+53, item.addition3)
		packet.data[55] = item.index
		packet.setUInt(index+54, item.enchantments[0])
		packet.setUInt(index+58, item.enchantments[1])
		packet.data[index+48] = inv.dye

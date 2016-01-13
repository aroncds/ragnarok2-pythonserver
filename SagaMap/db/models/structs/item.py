# -*- coding: utf-8 -*-

class Item:

	__slots__ = [
		'id', 'addition', 'questitem', 'equip_type', 'type', 'price',
		'unknow1', 'trade', 'drop', 'unknow3', 'unknow4', 'name', 'quest',
		'JobRequirement', 'WeaponRequirement', 'req_addition', 'max_stack',
		'max_dur', 'unknow2', 'skill_id', 'option_id', 'req_male', 'req_clv',
		'req_female', 'addition1', 'addition2', 'enchantments', 'index', 'dye'
	]

	def __init__(self, *args, **kwargs):
		for key, item in kwargs.items():
			setattr(self, key, item)

	def serialize(packet, inv, index):
		item = inv.item
		packet.setInt(index, item.id)
		packet.setUInt(index+4, 0)
		packet.setString(inv.creatorName, index+8, 32)
		packet.setUInt(index + 45, 0)
		packet.data[index+46] = item.trade
		packet.setUShort(index+47, inv.durability)
		packet.setUInt(index+49, item.addition1)
		packet.setUInt(index+51, item.addition2)
		packet.setUInt(index+53, item.addition3)
		packet.data[55] = item.index
		packet.setUInt(index+54, item.enchantments[0])
		packet.setUInt(index+58, item.enchantments[1])
		packet.data[index+48] = inv.dye

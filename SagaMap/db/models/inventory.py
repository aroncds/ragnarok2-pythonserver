from db import model
from manager.item import items


class InventoryItem(model.Model):
	table = 'inventory'
	primary_key = 'id'

	id = model.AutoID()
	charID = model.IntField()
	nameID = model.IntField()
	creatorName= model.CharField()
	equip = model.IntField()
	amount = model.IntField()
	durability = model.IntField()
	stone1 = model.IntField()
	stone2 = model.IntField()
	dye = model.IntField()

	@property
	def item(self):
	    return items.get(self.nameID, None)

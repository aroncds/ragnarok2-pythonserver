from db import model
from manager.itemmanager import items
import copy

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

	def getItem(self):
		item = copy.copy(items.get(self.nameID, None))
		item.durability = self.durability
		item.creatorName = self.creatorName
		item.stone1 = self.stone1
		item.stone2 = self.stone2
		item.amount = self.amount
		return item

from db import model


class Inventory(model.Model):
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

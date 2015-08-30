from db import model


class Weapon(model.Model):
	table = 'weapon'
	primary_key = 'charID'

	charID = model.IntField()
	name = model.CharField()
	level = model.IntField()
	type = model.IntField()
	augeSkillID = model.IntField()
	exp = model.IntField()
	durability = model.IntField()
	U1 = model.IntField()
	active = model.IntField()
	slot1 = model.IntField()
	slot2 = model.IntField()
	slot3 = model.IntField()
	slot4 = model.IntField()
	slot5 = model.IntField()
	slot6 = model.IntField()

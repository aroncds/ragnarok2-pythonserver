from db import model


class Skill(model.Model):
	table = 'skills'
	primary_key = 'id'

	id = model.AutoID()
	charID = model.IntField()
	type = model.IntField()
	skillID = model.IntField()
	exp = model.IntField()
	slot = model.IntField()

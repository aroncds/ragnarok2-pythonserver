# -*- coding: utf-8 -*-

from .base import Manager
from db.models.structs.npc import Npc
from db.model import IntField, CharField


class NpcManager(Manager):
	ID = IntField()
	Name = CharField()
	HP = IntField()
	SP = IntField()
	Level = IntField()
	CEXP = IntField()
	JEXP = IntField()
	WEXP = IntField()
	Def = IntField()
	Flee = IntField()
	AtkMin = IntField()
	Cri = IntField()
	Hit = IntField()
	ASPD = IntField()
	SightRange = IntField()
	Size = IntField()
	WalkSpeed = IntField()
	RunSpeed = IntField()
	LivingSpace = CharField()

	class Meta:
		db = 1
		key = 'ID'
		name = "npcdb"
		model = Npc
		dir_data = '../DB/MobDB.xml'

npcs = NpcManager()

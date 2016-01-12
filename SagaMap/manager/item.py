# -*- coding: utf-8 -*-

from .base import Manager
from db.model import IntField, CharField
from db.models.structs import Item


class ItemManager(Manager):
    id = IntField()
    addition = IntField()
    skill_id = IntField()
    questitem = IntField()
    equip_type = IntField()
    type = IntField()
    price = IntField()
    unknow1 = IntField()
    unknow2 = IntField()
    unknow3 = IntField()
    unknow4 = IntField()
    name = CharField()
    quest = IntField()
    JobRequirement = None
    WeaponRequirement = None
    req_addition = IntField()
    max_stack = IntField()
    max_dur = IntField()
    option_id = IntField()
    req_male = IntField()
    req_female = IntField()
    req_clv = IntField()

    class Meta:
        name = "itemdb"
        model = Item
        dir_data = "../DB/itemDB.xml"

items = ItemManager()

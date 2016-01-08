# -*- coding:utf-8 -*-

from xml.etree import ElementTree
from weakref import weakref

from db.models.item import Item


class ManagerLoadItens(object):
    def __init__(self):
        self.lista = None

    def create_item(self, lista):
        item = None
        for itemXML in lista:
            item = Item()
            fields = itemXML.getchildren()
            item.set_values(fields)
            yield item

    def load_item_data(self):
        with ElementTree.parse("../DB/itemDB.xml") as tree:
            root = tree.getroot()
            lista = root.getchildren()
            self.lista = {item.id: item for item in self.create_item(lista)}

_loaded_itens = ManagerLoadItens()
_loaded_itens.load_item_data()

items = weakref.proxy(_loaded_itens.lista)

from weakref import weakref

from db.models.item import Item

import xml.etree.ElementTree as ET


class ManagerLoadItens(dict):
    def create_item(self, lista):
        item = None
        for itemXML in lista:
            item = Item()
            fields = itemXML.getchildren()
            item.set_values(fields)
            yield item

    def load_item_data(self):
        with ET.parse("../DB/itemDB.xml") as tree:
            root = tree.getroot()
            lista = root.getchildren()
            self = {item.id: item for item in self.create_item(lista)}

_loaded_itens = ManagerLoadItens().load_item_data()
items = weakref.proxy(_loaded_itens)

from weakref import weakref

from db.models.item import Item

import xml.etree.ElementTree as ET

_items = {}
items = weakref.proxy(_items)


def load_item_data():
    with ET.parse("../DB/itemDB.xml") as tree:
        root = tree.getroot()
        lista = root.getchildren()

        for itemXML in lista:
            item = Item()
            fields = itemXML.getchildren()
            item.set_values(fields)
            _items[item.id] = item

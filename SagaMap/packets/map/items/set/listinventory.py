from packet import Packet
from db.models.structs.item import Item


class ListInventory(Packet):
	def __init__(self, numberItens):
		self.size = (10 + (67*numberItens))
		self.data = [0] * self.size
		self.setID(0x0502)
		self.data[9] = numberItens
		self.setLength()

	def setSortType(self, type):
		self.data[8] = type

	def setListItens(self, lista):
		for i, item in enumerate(lista.values()):
			Item.serialize(self, item, 10 + i * 67)

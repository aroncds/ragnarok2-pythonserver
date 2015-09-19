from packet import Packet
from manager.itemmanager import Item


class ListInventory(Packet):
	def __init__(self, numberItens):
		self.data = [0] * 10 + (67*numberItens)
		self.setID(0x0502)
		self.data[9] = numberItens
		self.setLength()

	def SetSortType(type):
		self.data[8] = type

	def setListItens(self, lista):
		for i, item in enumerate(lista):
			Item.serialize(self, item, 10 + i * 67)

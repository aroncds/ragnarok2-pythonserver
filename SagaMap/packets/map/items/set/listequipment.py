from packet import Packet
from db.models.structs.item import Item


class ListEquipment(Packet):
	def __init__(self):
		self.data = [0]*1096
		self.setID(0x0512)
		self.size = 1096
		self.setLength()

	def setEquipList(self, lista):
		for i, item in lista.items():
			Item.serialize(self, item, 8 + i * 68)
			self.data[8 + (i * 68 ) + 67] = 1

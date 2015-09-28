from packet import Packet


class ListEquipment(Packet):
	def __init__(self):
		self.data=[0]*1096
		self.setID(0x0512)
		self.size = 1096
		self.setLength()

	def setEquipList(lista):
		for i, item in enumerate(lista):
			Item.serialize(self, item, 8 + i * 68)

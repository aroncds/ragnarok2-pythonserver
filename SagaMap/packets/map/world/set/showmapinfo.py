from packet import Packet


class ShowMapInfo(Packet):
	def __init__(self):
		self.data = [0] * 264
		self.size = 264
		self.setID(0x0317)
		self.setLength()

	def setMapInfo(self, info):
		for i, v in enumerate(info):
			self.data[8+i] = v 

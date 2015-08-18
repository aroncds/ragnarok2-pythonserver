from Packet import Packet


class MapPong(Packet):
	def __init__(self):
		self.data = [0] * 8
		self.setID(0xFE03)
		self.size = 8
		self.setLength()

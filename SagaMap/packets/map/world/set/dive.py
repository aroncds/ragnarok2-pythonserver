from packet import Packet


class Dive(Packet):
	def __init__(self):
		self.data = [0] * 13
		self.setID(0x0320)
		self.size = 13
		self.setLength()

	def setDirection(self, value):
		self.data[8] = value

	def setOxygen(self, value):
		self.setUInt(9, value)
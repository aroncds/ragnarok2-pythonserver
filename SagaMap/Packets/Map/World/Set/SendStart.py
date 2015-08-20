from Packet import Packet


class SendStart(Packet):
	def __init__(self):
		self.data = [0] * 26
		self.setID(0x0301)
		self.size = 26
		self.setUnknow(0x0D)
		self.setChannel(1)
		self.setLength()

	def setUnknow(self, value):
		self.setUInt(8, value)

	def setMapID(self, value):
		self.data[12] = value

	def setChannel(self, value):
		self.data[13] = value

	def setLocation(self, x, y, z):
		self.setFloat(14, x)
		self.setFloat(18, y)
		self.setFloat(22, z)
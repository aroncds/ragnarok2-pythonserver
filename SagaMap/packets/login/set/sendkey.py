from packet import Packet


class SendKey(Packet):
	def __init__(self):
		self.data = [0] * 558
		self.size = 558
		self.setID(0x0201)
		self.setLength()

	def setKey(self, value):
		self.setBytes(value, 264, 16)

	def setColumn(self, value):
		self.data[520] = value

	def setRounds(self, value):
		self.data[524] = value

	def setDirection(self, value):
		self.data[528] = value
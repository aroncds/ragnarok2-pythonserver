from packet import Packet


class SendZeny(Packet):
	def __init__(self):
		self.data = [0] * 12
		self.setID(0x0515)
		self.size = 12
		self.setLength()

	def setZeny(self, value):
		self.setUInt(8, value)

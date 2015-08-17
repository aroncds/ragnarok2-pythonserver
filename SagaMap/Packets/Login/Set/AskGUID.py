from Packet import Packet

class AskGUID(Packet):
	size = 28
	
	def __init__(self):
		self.data = bytearray([0] * 28)
		self.setID(0x0202)
		self.setLength()


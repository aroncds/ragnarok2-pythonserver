from packet import Packet


class SendChat(Packet):
	def __init__(self):
		self.data = [0] * 41
		self.setID(0x0401)

	def setTypeMessage(self, t):
		self.data[8] = t

	def setName(self, name):
		self.setString(name, 9, 32)

	def setMessage(self, message):
		self.setStringArrayResize(message, 44, 127)
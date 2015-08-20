from Packet import Packet


class Identify(Packet):
	def __init__(self):
		self.data = [0] * 260
		self.setID(0xff01)
		self.size = 260
		self.setLength()

	def setLoginPassword(self, password):
		self.setString(password, 8, 24)

	def setWorldName(self, name):
		self.setString(name, 58, 24)

	def setHostedMaps(self, list):
		for i in range(len(list)):
			self.setInt(108 + (4 * i), list[i])

	def setIP(self, ip):
		self.setString(ip, 228, 28)

	def setPort(self, port):
		self.setUShort(258, port)
from packet import Packet


class ActorPlayerInfo(Packet):
	def __init__(self):
		self.data = [0] * 81
		self.setID(0x0303)
		self.size = 81
		self.setLength()

	def setActorID(self, id):
		self.setUInt(8, id)

	def setName(self, name):
		self.setString(name, 12, 32)

	def setLocation(self, x,y,z):
		self.setFloat(46, x)
		self.setFloat(50, y)
		self.setFloat(54, z)

	def setYaw(self, yaw):
		self.setFloat(58, yaw)

	def setRace(self, race):
		self.data[62] = race
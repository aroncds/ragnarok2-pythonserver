from packet import Packet


class CharStatus(Packet):
	def __init__(self):
		self.data = [0] * 35
		self.setID(0x0308)
		self.size = 35
		self.setLength()

	def setJob(self, job):
		self.data[12] = job

	def setExp(self, cExp, jExp):
		self.setUInt(8, cExp)
		self.setUInt(13, jExp)

	def setHP(self, current, max):
		self.setUShort(17, current)
		self.setUShort(19, max)

	def setSP(self, current, max):
		self.setUShort(21, current)
		self.setUShort(23, max)

	def setLC(self, current, max):
		self.data[25] = current
		self.data[26] = max

	def setLP(self, current, max):
		self.data[27] = current
		self.data[28] = max

	def setVisibleField(self, u):
		self.setUShort(33, u)

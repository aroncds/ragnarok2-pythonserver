from packet import Packet
from utils.math import Vector3


class MoveStart(Packet):
	def getPosition(self):
		vec = Vector3(0,0,0)
		vec.X = self.getFloat(8)
		vec.Y = self.getFloat(12)
		vec.Z = self.getFloat(16)
		return vec

	def getAcceleration(self):
		vec = Vector3(0,0,0)
		vec.X = self.getFloat(20)
		vec.Y = self.getFloat(24)
		vec.Z = self.getFloat(28)
		return vec

	def getU1(self):
		return self.getUInt(32)

	def getYaw(self):
		return self.getInt(36)

	def getDelayTime():
		return self.getUInt(40)

	def getMoveType():
		return self.data[44]

	def getUnknow():
		return self.getInt(45)

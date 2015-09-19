from utils.math import Vector3


class Actor:
	position = Vector3(0,0,0)
	yaw = 0
	status = 0
	buff = {}
	debuff = {}

	@property
	def X(self):
	    return self.position.X

	@property
	def Y(self):
	    return self.position.Y

	@property
	def Z(self):
	    return self.position.Z

	@X.setter
	def X(self, value):
		self.x = value
		self.position.X = value

	@Y.setter
	def Y(self, value):
		self.y = value
		self.position.Y = value

	@Z.setter
	def Z(self, value):
		self.z = value
		self.position.Z = value
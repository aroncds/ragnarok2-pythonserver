import math


class Vector2:
	def __init__(self):
		self.X = 0
		self.Y = 0

	def __init__(self, x, y):
		self.X = x
		self.Y = y

	def __mul__(self, target):
		if(isinstance(target, Vector2)):
			self.X *= target.X
			self.Y *= target.Y
			return self

	def __add__(self, target):
		if(isinstance(target, Vector2)):
			self.X += target.X
			self.Y += target.Y
			return self

	def __sub__(self,target):
		if(isinstance(target,Vector2)):
			self.X -= target.X
			self.Y -= target.Y
			return self

	def __eq__(self, target):
		if(isinstance(target,Vector2)):
			return self.X == target.X and self.Y == target.Y
		return False

	def __str__(self):
		return "Vector2({x},{y},{z})".format(self.X, self.Y, self.Z)


class Vector3:
	def __init__(self):
		self.X = 0
		self.Y = 0
		self.Z = 0

	def __init__(self, x, y, z):
		self.X = x
		self.Y = y
		self.Z = z

	def __mul__(self, target):
		if(isinstance(target, Vector3)):
			self.X *= target.X
			self.Y *= target.Y
			self.Z *= target.Z
			return self

	def __add__(self, target):
		if(isinstance(target, Vector3)):
			self.X += target.X
			self.Y += target.Y
			self.Z += target.Z
			return self

	def __sub__(self,target):
		if(isinstance(target,Vector3)):
			self.X -= target.X
			self.Y -= target.Y
			self.Z *= target.Z
			return self

	def __eq__(self, target):
		if(isinstance(target,Vector3)):
			return self.X == target.X and \
					self.Y == target.Y and \
					self.Z == target.Z
		return False

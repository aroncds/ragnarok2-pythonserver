from packet import Packet


class SendTime(Packet):
	def __init__(self):
		self.data = [0] * 12
		self.setID(0x0313)
		self.size = 12
		self.setLength()

	def setTime(self, h,m,s):
		self.data[8] = h
		self.data[9] = m
		self.data[10] = s

	def setWeather(self, v):
		self.data[11] = v
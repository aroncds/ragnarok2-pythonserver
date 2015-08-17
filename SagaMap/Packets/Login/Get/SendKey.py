from Packet import Packet


class SendKey(Packet):
	def getKey(self):
		dbytes = self.data[264:280]
		return dbytes
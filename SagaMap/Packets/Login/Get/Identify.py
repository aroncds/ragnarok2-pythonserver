from Packet import Packet


class Identify(Packet):
	def getPacketSessionId(self):
		return self.getUint(8)
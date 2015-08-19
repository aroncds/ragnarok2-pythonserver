from Packet import Packet


class IdentAnswer(Packet):
	def getError(self):
		return self.data[8]
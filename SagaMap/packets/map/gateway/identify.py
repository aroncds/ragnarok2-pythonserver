from packet import Packet


class GatewayIdentify(Packet):
	def getCharID(self):
		return self.getUInt(8)

	def getValidationKey(self):
		return self.getUInt(12)

	def getGatewaySessionID(self):
		return self.getUInt(16)
from Packet import Packet

def OnPacketData(id, data, client, dict_packet):
	if id in dict_packet:
		packet_class = dict_packet[id]['class']()
		packet_class.data = data
		packet = dict_packet[id]['function'](packet_class, client)
	else:
		print "Unknow package ID: " + str(id) + " \n with data length: " + str(len(data))


class Client(object):
	sessionID = 0
	connection = None

	def __init__(self, connection):
		self.connection = connection

	def sendPacket(self, pck):
		try:
			if(self.connection):
				pck.setSessionID(self.sessionID)
				print pck.data
				self.connection.send(bytearray(pck.data))
		except:
			print "Ocorreu um erro ao enviar o pacote"


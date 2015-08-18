import socket
import thread
import time

from Packet import Packet
from Packets.Login.List import dict_packet

host = ""
port = None
key = None
sessionID = 0
loginServer = None


class LoginClient(object):
	sck = None
	key = 0
	sessionID = 0

def startConnectionLoginServer():
	login = LoginClient()

	loginServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	loginServer.connect((host, port))

	while 1:
		msg = loginServer.recv(1024)

		start_time = time.clock()
		data = bytearray(msg)

		pck = Packet()
		pck.data = data

		id = pck.getPacketID()
		buffer = OnEventPacketData(data, id, login)

		if(buffer):
			loginServer.send(buffer)

		end_time = time.clock() - start_time
		print "Time: " + str(end_time)


def OnEventPacketData(data, id, client):
	if id in dict_packet:
		packet_class = dict_packet[id]['class']()
		packet_class.data = data
		packet = dict_packet[id]['function'](packet_class)
		if(hasattr(packet, "data")):
			return (bytearray(packet.data))
	else:
		print "Unknow package ID: " + id + " \n with data length: " + str(len(data))

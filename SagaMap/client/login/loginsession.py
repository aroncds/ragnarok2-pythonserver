import socket
import time

from packet import Packet
from packets.login.List import dict_packet

from client.client import Client

host = ""
port = None
key = None
sessionID = 0
loginServer = None


class LoginClient(Client):
	pass


def startConnectionLoginServer():
	loginServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	loginServer.connect((host, port))

	login = LoginClient(loginServer)

	while 1:
		msg = loginServer.recv(1024)

		start_time = time.clock()
		data = bytearray(msg)

		pck = Packet()
		pck.data = data

		id = pck.getPacketID()

		login.OnPacketData(id, data, dict_packet)

		end_time = time.clock() - start_time
		print("Time: " + str(end_time))

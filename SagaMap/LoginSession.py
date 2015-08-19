import socket
import thread
import time

from Packet import Packet
from Packets.Login.List import dict_packet

from Client.Client import Client, OnPacketData

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

		OnPacketData(id, data, login, dict_packet)

		end_time = time.clock() - start_time
		print "Time: " + str(end_time)

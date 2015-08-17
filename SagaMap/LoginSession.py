import socket
import thread
import struct
from Packet import Packet

from Packets.Login.Get import SendKey
from Packets.Login.Set import AskGUID, SendKey as ServerKey, Identify

import Encryption


host = ""
port = None
loginServer = None
sessionID = 0
key = None

def startConnectionLoginServer():
	loginServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	loginServer.connect((host,port))

	while 1:
		msg = loginServer.recv(1024)
		data = bytearray(msg)

		pck = Packet()
		pck.data = data

		StaticKey = [0x40, 0x21, 0xBF, 0xE4, 0xB0, 0xC7, 0xB8, 0xF0, 0xB8, 0xA3, 0xB0, 0xDA, 0xC1, 0xF6, 0x24, 0x00]
		id = pck.getPacketID()

		if(id == 0x0201):
			pck = SendKey.SendKey()
			pck.data = data

			serverPck = ServerKey.SendKey()

			serverPck.setKey(Encryption.GenerateDecExpKey(StaticKey))
			serverPck.setColumn(4)
			serverPck.setRounds(10)
			serverPck.setDirection(2)
			
			loginServer.send(bytearray(serverPck.data))

		elif (id == 0x0202):
			pck = Identify.Identify()
			pck.setLoginPassword("secret")
			pck.setWorldName("Saga1")
			pck.setHostedMaps([1,2,3,4,5,6,7,8])
			pck.setIP("127.0.0.1")
			pck.setPort(3011)

			loginServer.send(bytearray(pck.data))
		else:
			import ipdb; ipdb.set_trace()


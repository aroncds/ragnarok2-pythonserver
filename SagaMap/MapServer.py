import socket
from threading import Thread

import settings
import LoginSession

from Packet import Packet
from Manager.mapclientmanager import MapClientManager

print("Comecando a inicializar o servidor")
mapmanager = MapClientManager()

def startServer():
	print("Iniciando conexao com servidor de Login...")

	LoginSession.host = settings.LOGIN_HOST
	LoginSession.port = settings.LOGIN_PORT
	th = Thread(target=LoginSession.startConnectionLoginServer, args=[])
	th.start()

	print("Iniciando servidor de mapa")

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind((settings.HOST, settings.PORT))
	tcp.listen(1)

	while 1:
		con, cliente = tcp.accept()
		thm = Thread(target=map_server, args=[con, cliente])
		thm.start()

from Client.Map.MapClient import MapClient
from Packets.Map.List import dict_packets
def map_server(connection, client):
	local_client = MapClient(connection)
	mapmanager.set_client(local_client)

	while 1:
		msg = connection.recv(1024)
		pck = Packet()
		pck.data = bytearray(msg)

		local_client.OnPacketData(pck.getPacketID(), pck.data, dict_packets)

	Thread.exit()


startServer()
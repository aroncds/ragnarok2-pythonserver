import socket
import thread

import settings
import loginsession as LoginSession

from packet import Packet

from client.map.mapclient import MapClient
from packets.map.List import dict_packets

from manager.itemmanager import load_item_data

print("Comecando a inicializar o servidor")

def startServer():
	print("Carregando Items...")
	load_item_data()

	print("Iniciando conexao com servidor de Login...")

	LoginSession.host = settings.LOGIN_HOST
	LoginSession.port = settings.LOGIN_PORT
	thread.start_new_thread(LoginSession.startConnectionLoginServer, ())

	print("Iniciando servidor de mapa")

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind((settings.HOST, settings.PORT))
	tcp.listen(1)

	while 1:
		con, cliente = tcp.accept()
		thread.start_new_thread(map_server, (con, cliente))

	tcp.close()

def map_server(connection, client):
	local_client = MapClient(connection)

	while 1:
		msg = connection.recv(1024)
		pck = Packet()
		pck.data = bytearray(msg)

		local_client.OnPacketData(pck.getPacketID(), pck.data, dict_packets)

startServer()

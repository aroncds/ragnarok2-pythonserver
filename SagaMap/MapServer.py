import socket
import thread

import settings
import LoginSession

from Packet import Packet

print "Comecando a inicializar o servidor"

def startServer():
	print "Iniciando conexao com servidor de Login..."

	LoginSession.host = settings.LOGIN_HOST
	LoginSession.port = settings.LOGIN_PORT
	thread.start_new_thread(LoginSession.startConnectionLoginServer, ())

	print "Iniciando servidor de mapa"

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind((settings.HOST, settings.PORT))
	tcp.listen(1)

	while 1:
		con, cliente = tcp.accept()
		thread.start_new_thread(map_server, (con, cliente))

from Client.Client import OnPacketData, Client
from Packets.Map.List import dict_packets
def map_server(connection, client):
	client = Client(connection)
	while 1:
		msg = connection.recv(1024)
		pck = Packet()
		pck.data = bytearray(msg)

		OnPacketData(pck.getPacketID(), pck.data, client, dict_packets)

		import ipdb; ipdb.set_trace()

	Thread.exit()


startServer()
import socket
import thread

import settings
import LoginSession

print "Comecando a inicializar o servidor"

def startServer():
	LoginSession.host = settings.LOGIN_HOST
	LoginSession.port = settings.LOGIN_PORT
	thread.start_new_thread(LoginSession.startConnectionLoginServer, ())

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind((settings.HOST, settings.PORT))
	tcp.listen(1)

	while 1:
		con, cliente = tcp.accept()
		thread.start_new_thread(client, tuple(con, cliente))


def client(connection, client):
	while 1:
		msg = connection.recv(1024)
		print msg


startServer()
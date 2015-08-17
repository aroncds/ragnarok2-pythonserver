import socket
import cffi
import time
import thread
import LoginSession

# Variables
host = ""
port = 3011

print "Comecando a inicializar o servidor"

def startServer():
	LoginSession.host = "127.0.0.1"
	LoginSession.port = 6000
	thread.start_new_thread(LoginSession.startConnectionLoginServer, ())

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind((host,port))
	tcp.listen(1)

	while 1:
		con, cliente = tcp.accept()
		thread.start_new_thread(client, tuple(con, cliente))


def client(connection, client):
	while 1:
		msg = connection.recv(1024)
		print msg


startServer()
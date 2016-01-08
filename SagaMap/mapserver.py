from socket import socket, AF_INET, SOCK_STREAM

from multiprocessing import Process
from threading import Thread

from client.login.loginsession import LoginClient
from client.map.mapclient import MapClient

from packet import Packet
from packets.map.List import dict_packets
from manager.itemmanager import load_item_data

from settings import HOST, PORT

print("Comecando a inicializar o servidor")
load_item_data()


class StartServer(Process):
    def __init__(self):
        self.threads = []

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.socket.listen(1)

        self.login_client = LoginClient()
        self.login_client.start()

        super(StartServer, self).__init__()

    def run(self):
        while 1:
            con, client = self.socket.accept()
            mapserver = MapServer(con, client)
            mapserver.start()

            self.threads.append(mapserver)

    def __del__(self):
        for thread in self.threads:
            thread.stop()


class MapServer(MapClient, Thread):
    def __init__(self, connection, client):
        MapClient.__init__(self, connection)
        Thread.__init__(self)
        self.connected = 1

    def run(self):
        while self.connected:
            msg = self.connection.recv(1024)
            pck = Packet()
            pck.data = bytearray(msg)
            self.OnPacketData(pck.getPacketID(), pck.data, dict_packets)


if __name__ == "__main__":
    start_server = StartServer()
    start_server.start()

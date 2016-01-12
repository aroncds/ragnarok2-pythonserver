from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from packet import Packet
from client.client import Client
from packets.login.List import dict_packet
from settings import LOGIN_HOST, LOGIN_PORT


class LoginClient(Client, Thread):
        def __init__(self):
            import time
            running = True
            self.connection = socket(AF_INET, SOCK_STREAM)

            while running:
                try:
                    self.connection.connect((LOGIN_HOST, LOGIN_PORT))
                    running = False
                except Exception as e:
                    print("#---Login Server: Failed---#")
                    print(e)

                    running = True
                    time.sleep(5)

        def run(self):
            while 1:
                msg = self.connection.recv(1024)
                data = bytearray(msg)
                pck = Packet()
                pck.data = data
                self.onpacketdata(pck.getPacketID(), data, dict_packet)

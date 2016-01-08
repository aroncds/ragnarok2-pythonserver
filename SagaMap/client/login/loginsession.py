from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from packet import Packet
from client.client import Client
from packets.login.List import dict_packet
from settings import LOGIN_HOST, LOGIN_PORT


class LoginClient(Client, Thread):
        def __init__(self):
            self.connection = socket(AF_INET, SOCK_STREAM)
            self.connection.connect(LOGIN_HOST, LOGIN_PORT)

        def run(self):
            while 1:
                msg = self.connection.recv(1024)
                data = bytearray(msg)
                pck = Packet()
                pck.data = data
                self.onpacketdata(pck.getPacketID(), data, dict_packet)

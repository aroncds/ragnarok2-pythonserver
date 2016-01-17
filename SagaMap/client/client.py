# -*- coding: utf-8 -*-
from packets import packets


class Client(object):
    sessionID = 0
    __connection = None

    def __init__(self, connection=None):
        self.connection = connection

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        if not self.__connection:
            self.__connection = value

    def sendpacket(self, pck):
        try:
            if(self.connection):
                pck.setSessionID(self.sessionID)
                self.__connection.send(bytearray(pck.data))
        except Exception as e:
            print("Ocorreu um erro ao enviar o pacote: %s" % e)

    def onpacketdata(self, id_packet, data, dict_packet):
        info_packet = packets.get(id_packet)
        if data:
            packet_class = info_packet['class']()
            packet_class.data = data
            info_packet['function'](self, packet_class)

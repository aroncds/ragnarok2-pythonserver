# -*- coding: utf-8 -*-


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
        if id_packet in dict_packet:
            packet_class = dict_packet[id_packet]['class']()
            packet_class.data = data
            dict_packet[id_packet]['function'](
                self,
                packet_class
            )
        else:
            print(
                "Unknow package ID: "\
                + str(id_packet) + " with data length: "\
                + str(len(data))
            )

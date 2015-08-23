from Client.Client import Client
from Packets.Map.World.Set.SendStart import SendStart


def OnIdentify(pck, client):
	charID = pck.getCharID()
	print "Char: " + str(charID)
	client.sessionID = pck.getGatewaySessionID()

	sendStart = SendStart()
	sendStart.setMapID(1)
	sendStart.setLocation(0.0,0.0,0.0)

	client.sendPacket(sendStart)

from DB import model


class Char(model.Model):
	table = 'char'
	charID = model.AutoField()
	name = model.CharField()


class MapClient(Client):
	char = None
	status = ""

from Client.Client import Client
from Packets.Map.World.Set.SendStart import SendStart


def OnIdentify(pck, client):
	charID = pck.getCharID()
	client.sessionID = pck.getGatewaySessionID()

	sendStart = SendStart()
	sendStart.setMapID(1)
	sendStart.setLocation(0.0,0.0,0.0)

	client.sendPacket(sendStart)

from packets.map.world.set import actorplayerinfo, sendstart, charstatus
from manager.mapclientmanager import mapmanager
from db.models.char import CharDB
from client.client import Client

from actors.actorpc import ActorPlayer


class MapClient(Client):
	char = None
	status = ""

	def setChar(self, char):
		self.char = char


def OnIdentify(client, pck):
	charID = pck.getCharID()
	
	client.sessionID = pck.getGatewaySessionID()

	client.char = ActorPlayer(charID)
	
	sStart = sendstart.SendStart()
	sStart.setMapID(client.char.mapID)
	sStart.setLocation(
		client.char.X,
		client.char.Y,
		client.char.Z
	)

	mapmanager.set_client(client)
	client.sendpacket(sStart)

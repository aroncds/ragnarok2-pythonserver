from packets.map.world.set import actorplayerinfo, sendstart, charstatus
from packets.map.gateway.identify import GatewayIdentify
from actors.actorpc import ActorPlayer
from decorators.packets import onpacket
from db.models.char import CharDB
from client.client import Client


class MapClient(Client):
	char = None
	status = ""

	def setChar(self, char):
		self.char = char


@onpacket(GatewayIdentify, 0x010C)
def OnIdentify(client, pck):
	charID = pck.getCharID()
	client.sessionID = pck.getGatewaySessionID()
	client.char = ActorPlayer(charID)
	sStart = sendstart.SendStart()
	sStart.setMapID(client.char.mapID)
	sStart.setLocation(client.char.X ,client.char.Y ,client.char.Z)
	client.sendpacket(sStart)

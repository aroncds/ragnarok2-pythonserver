from packets.map.world.set import actorplayerinfo, sendstart, charstatus
from manager.mapclientmanager import mapmanager
from db.models.char import CharDB
from client.client import Client
from .mapclient_map import *
from .mapclient_items import *


class MapClient(Client):
	char = None
	status = ""

	def setChar(self, char):
		self.char = char


def OnIdentify(client, pck):
	charID = pck.getCharID()
	
	client.sessionID = pck.getGatewaySessionID()

	client.char = CharDB(charID)

	sStart = sendstart.SendStart()
	sStart.setMapID(client.char.mapID)
	sStart.setLocation(
		client.char.x,
		client.char.y,
		client.char.z
	)

	mapmanager.set_client(client)
	client.sendPacket(sStart)

from Client.Client import Client
from Packets.Map.World.Set.SendStart import SendStart

from DB.models.char import CharDB

from Packets.Map.World.Set import ActorPlayerInfo
from decorators.status import MapLoaded


class MapClient(Client):
	char = None
	status = ""

	def setChar(self, char):
		self.char = char

	def SendStatus(self):
		actor = ActorPlayerInfo.ActorPlayerInfo()
		actor.setName(self.char.name)
		actor.setActorID(self.char.charID)
		actor.setLocation(
			self.char.x,
			self.char.y,
			self.char.z
		)
		actor.setYaw(self.char.yaw)
		actor.setRace(self.char.race)
		self.SendPacket(actor)

		return self

	def OnIdentify(self, pck):
		charID = pck.getCharID()
		
		self.sessionID = pck.getGatewaySessionID()

		char = CharDB(charID)
		setattr(self, 'char', char)

		sendStart = SendStart()
		sendStart.setMapID(char.mapID)
		sendStart.setLocation(char.x,char.y,char.z)

		self.sendPacket(sendStart)
		return self

	def OnSendMapLoaded(self, pck):
		self.SendStatus()
		return self


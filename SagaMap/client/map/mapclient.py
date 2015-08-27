from packets.map.world.set import actorplayerinfo, sendstart
from decorators.status import MapLoaded
from db.models.char import CharDB
from client.client import Client


class MapClient(Client):
	char = None
	status = ""

	def setChar(self, char):
		self.char = char

	def SendStatus(self):
		print(id(self))
		import ipdb; ipdb.set_trace()

		actor = actorplayerinfo.ActorPlayerInfo()
		actor.setName(self.char.name)
		actor.setActorID(self.char.charID)
		actor.setLocation(
			self.char.x,
			self.char.y,
			self.char.z
		)

		print self.char.name

		actor.setYaw(self.char.yaw)
		actor.setRace(self.char.race)
		self.sendPacket(actor)

	def OnIdentify(self, pck):
		charID = pck.getCharID()
		
		self.sessionID = pck.getGatewaySessionID()

		self.char = CharDB(charID)

		print(id(self))

		sStart = sendstart.SendStart()
		sStart.setMapID(self.char.mapID)
		sStart.setLocation(
			self.char.x,
			self.char.y,
			self.char.z
		)

		self.sendPacket(sStart)

	def OnSendMapLoaded(self, pck):
		self.SendStatus()

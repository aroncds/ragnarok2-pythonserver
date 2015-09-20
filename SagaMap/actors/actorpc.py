from .actor import Actor

from db.model import ManagerModel
from db.models.char import CharDB
from db.models.inventory import Inventory


class ActorPlayer(Actor, CharDB):
	inventory = []
	skills = []
	weapons = []
	friends = []
	blacklist = []

	def __init__(self, actorID=None):
		if actorID:
			super(ActorPlayer, self).__init__(actorID)

			self.position.X = self.x
			self.position.Y = self.y
			self.position.Z = self.z

			self.inventory = [
				item.getItem() for item in ManagerModel(Inventory).filter(
					charID=actorID
				)
			]

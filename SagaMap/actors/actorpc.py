from .actor import Actor

from db.model import ManagerModel
from db.models.char import CharDB
from db.models.inventory import InventoryItem


class Inventory(object):
	_equipment = {}
	_inventory = {}
	_storage = {}

	@property
	def items(self):
	    return self._items

	@property
	def equipment(self):
	    return self._equipment

	@property
	def inventory(self):
	    return self._inventory
	
	@items.setter
	def items(self, value):
		self._inventory ={
			item.nameID:item.getItem() for item in value if item.equip==-1
		}

		self._equipment ={
			item.equip:item.getItem() for item in value if item.equip!=-1
		}


class ActorPlayer(Actor, CharDB):
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

			self.inventory = Inventory()

			self.inventory.items = ManagerModel(InventoryItem).filter(
				charID=actorID
			)

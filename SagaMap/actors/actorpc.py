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
			obj.nameID:obj for obj in value if obj.equip==-1
		}

		self._equipment ={
			obj.equip:obj for obj in value if obj.equip!=-1
		}


class ActorPlayer(Actor, CharDB):

	def __init__(self, actorID=None):
		if actorID:
			CharDB.__init__(self, actorID)

			self.position.X = self.x
			self.position.Y = self.y
			self.position.Z = self.z

			self.inventory = Inventory()

			self.inventory.items = InventoryItem.objects.filter(
				charID=actorID
			)


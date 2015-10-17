from .actor import Actor

from db.model import ManagerModel
from db.models.char import CharDB
from db.models.inventory import InventoryItem
from db.models.weapon import Weapon
from db.models.skills import Skill


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


class Skills(object):
	_battleskills = {}
	_livingskills = {}
	_specialskills = {}

	@property
	def battleskills(self):
	    return self._battleskills
	
	@property
	def livingskills(self):
	    return self._livingskills
	
	@property
	def specialskills(self):
	    return self._specialskills

	@property
	def lista(self):
	    raise "No possible"

	@lista.setter
	def lista(self, value):
		self._battleskills ={
			obj.skillID:obj for obj in value if obj.type==0
		}

		self._livingskills ={
			obj.skillID:obj for obj in value if obj.type==2
		}

		self._specialskills ={
			obj.skillID:obj for obj in value if obj.type==3
		}
	


class ActorPlayer(Actor, CharDB):

	def __init__(self, actorID=None):
		if actorID:
			CharDB.__init__(self, actorID)

			self.position.X = self.x
			self.position.Y = self.y
			self.position.Z = self.z

			self.inventory = Inventory()
			self.skills = Skills()

			self.inventory.items = InventoryItem.objects.filter(
				charID=actorID
			)

			self.skills.lista = Skill.objects.filter(
				charID=actorID
			)

			self.weapons = Weapon.objects.filter(
				charID=actorID
			)


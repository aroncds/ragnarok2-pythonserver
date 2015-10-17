from packet import Packet


class WeaponList(Packet):
	def __init__(self):
		self.data = [0]*383
		self.setID(0x0510)
		self.size = 383
		self.setLength()

	def setWeapons(self, lista):
		for i, weapon in enumerate(lista):
			index = i * 75  + 8 
			self.setString(weapon.name, index, 24)
			self.data[index+24] = weapon.level
			self.setUInt(index+25, weapon.exp)
			self.data[index+29] = weapon.type
			self.setUShort(index+30, weapon.durability)
			self.setUShort(index+32, weapon.U1)
			self.setUInt(index+34, weapon.augeSkillID)
			self.setUInt(index+38, weapon.slot1)
			self.setUInt(index+42, weapon.slot2)
			self.setUInt(index+46, weapon.slot3)
			self.setUInt(index+50, weapon.slot4)
			self.setUInt(index+54, weapon.slot5)
			self.setUInt(index+58, weapon.slot6)
			self.setUInt(index+62, weapon.slot7)
			self.setUInt(index+66, weapon.slot8)
			self.setUInt(index+70, 0)
			self.data[index + 74] = weapon.active

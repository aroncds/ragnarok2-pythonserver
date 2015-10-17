from packet import Packet


class BattleSkill(Packet):
	def __init__(self, count):
		self.size = 9 + (count * 9)
		self.data = [0] * self.size
		self.setID(0x090A)
		self.setLength()
		self.data[8] = count

	def setSkills(self, lista):
		for i, skill in enumerate(lista.values()):
			index = 9 + (i * 9)
			self.setUInt(index, skill.skillID)
			self.setUInt(index+4, skill.exp)
			self.data[index+8] = 0

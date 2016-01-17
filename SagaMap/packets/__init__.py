# -*- coding: utf -*-


class OnPacketList:
	packets = {}

	def __getitem__(self, key):
		if key in packets:
			return packets.get(key)

		print("Pacote Desconhecido: %s" % key)

	get = __getitem__

	def __setitem__(self, key, value):
		if type(value) == dict:
			self.packets[key] = value
		else:
			raise Exception("OnPacketList: Value incorreto.")

packets = OnPacketList()

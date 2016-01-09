RANGE_DEFAULT = 10000

class Map:
	def __init__(self, map_id, name):
		self.name = name
		self.map_id = map_id
		self.actors = {}

	def contains_actor(self, actor):
		if actor.id in self.actors
			return True
		return False

	def add_actor(self, actor):
		if not self.contains_actor(actor):
			self.actors[actor.id] = actor

	def remove_actor(self, actor):
		if self.contains_actor(actor):
			del self.actors[actor.id]

	def send_packet_all_actors(self, packet):
		for actor in self.actors.values():
			actor.sendpacket(packet)                                                                                                                       

	def send_packet_all_actors_in_range(self, packet):
		pass
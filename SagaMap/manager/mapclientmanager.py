class MapClientManager(object):
	clients = []

	def set_client(self, client):
		self.clients.append(client)
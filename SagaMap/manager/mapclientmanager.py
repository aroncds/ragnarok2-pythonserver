class MapClientManager(object):
    clients = {}

    def set_client(self, client):
        self.clients[client.sessionID] = client

    def __unicode__(self):
        return self.clients

mapmanager = MapClientManager()

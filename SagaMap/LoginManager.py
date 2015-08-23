import Encryption

from Packets.Login.Set import (
	SendKey as ServerKey, Identify, MapPong
)

StaticKey = [
	0x40, 0x21, 0xBF, 0xE4, 0xB0, 0xC7, 0xB8,0xF0,
	0xB8, 0xA3, 0xB0, 0xDA, 0xC1, 0xF6, 0x24, 0x00
]

def OnSendKey(client, data):
	key = data.getKey()

	serverPck = ServerKey.SendKey()
	serverPck.setKey(Encryption.GenerateDecExpKey(StaticKey))
	serverPck.setColumn(4)
	serverPck.setRounds(10)
	serverPck.setDirection(2)
	
	client.sendPacket(serverPck)

def OnIdentify(client, data):
	import settings
	pck = Identify.Identify()
	pck.setLoginPassword(settings.LOGIN_PASSWORD)
	pck.setWorldName(settings.WORLD_NAME)
	pck.setHostedMaps(settings.HOSTED_MAPS)
	pck.setIP(settings.HOST)
	pck.setPort(settings.PORT)

	client.sendPacket(pck)

def OnMapPing(client, data):
	pck = MapPong.MapPong()
	pck.setSessionID(client.sessionID)
	client.sendPacket(pck)

def OnIdentAnswer(client, data):
	erro = data.getError()

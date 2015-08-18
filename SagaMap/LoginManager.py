import Encryption

from Packets.Login.Set import (
	AskGUID, SendKey as ServerKey, Identify, MapPong
)

StaticKey = [
	0x40, 0x21, 0xBF, 0xE4, 0xB0, 0xC7, 0xB8,0xF0,
	0xB8, 0xA3, 0xB0, 0xDA, 0xC1, 0xF6, 0x24, 0x00
]

def OnSendKey(data):
	key = data.getKey()

	serverPck = ServerKey.SendKey()
	serverPck.setKey(Encryption.GenerateDecExpKey(StaticKey))
	serverPck.setColumn(4)
	serverPck.setRounds(10)
	serverPck.setDirection(2)
	return serverPck

def OnIdentify(data):
	import settings
	pck = Identify.Identify()
	pck.setLoginPassword(settings.LOGIN_PASSWORD)
	pck.setWorldName(settings.WORLD_NAME)
	pck.setHostedMaps(settings.HOSTED_MAPS)
	pck.setIP(settings.HOST)
	pck.setPort(settings.PORT)
	return pck

def OnMapPing(data):
	pck = MapPong.MapPong()
	pck.setSessionID(0)
	return pck

def OnLoginIdentify(data):
	print "dasd"
	
	#sessionId = data.getPacketSessionId()
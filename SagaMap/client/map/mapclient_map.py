from packets.map.world.set import (
	actorplayerinfo, sendstart, charstatus, dive, sendtime, showmapinfo
)
from manager.mapclientmanager import mapmanager
from .mapclient_items import SendZeny
from .mapclient_chat import SendChatRed


def OnSendMapLoaded(client, pck):
	SendTimeWeather(client)
	SendStatus(client)
	SendCharStatus(client)
	SendZeny(client)
	SendChatRed(client, "asdsadssa")
	SendMapInfo(client, None)

def SendStatus(client):
	actor = actorplayerinfo.ActorPlayerInfo()
	actor.setName(client.char.name)
	actor.setActorID(client.sessionID)
	actor.setLocation(
		client.char.x,
		client.char.y,
		client.char.z
	)
	actor.setYaw(client.char.yaw)
	actor.setRace(client.char.race)
	actor.setFace(client.char.face)
	actor.setDetails(client.char.details)
	actor.setInventoryContainerSize(100)
	actor.setStorageContainerSize(100)
	actor.setSlotsWeaponUnlocked(1)
	print actor.data
	client.sendPacket(actor)

def SendCharStatus(client):
	charStatus = charstatus.CharStatus()
	charStatus.setJob(client.char.job)
	charStatus.setExp(client.char.cEXP, client.char.jEXP)
	charStatus.setHP(client.char.HP, client.char.maxHP)
	charStatus.setSP(client.char.SP, client.char.maxSP)
	charStatus.setLC(client.char.LC, client.char.maxLC)
	charStatus.setLP(client.char.LP, client.char.maxLP)
	charStatus.setVisibleField(1)
	client.sendPacket(charStatus)
	
def OnDiveUP(client, packet):
	pck = dive.Dive()
	pck.setDirection(1)
	pck.setOxygen(client.char.LC)
	client.sendPacket(pck)

def SendTimeWeather(client):
	pck = sendtime.SendTime()
	pck.setTime(4,4,4)
	pck.setWeather(2)
	client.sendPacket(pck)

def SendMapInfo(client, map):
	pck = showmapinfo.ShowMapInfo()
	client.sendPacket(pck)
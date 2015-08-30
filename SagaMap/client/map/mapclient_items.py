from packet import Packet
from packets.map.items.set import sendzeny


def SendZeny(client):
	pck = sendzeny.SendZeny()
	pck.setZeny(client.char.zeny)
	client.sendPacket(pck)
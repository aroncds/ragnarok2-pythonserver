from packet import Packet
from packets.map.items.set import sendzeny, listinventory


def SendZeny(client):
	pck = sendzeny.SendZeny()
	pck.setZeny(client.char.zeny)
	client.sendPacket(pck)

def SendListInventory(client):
	lista = client.char.inventory
	lenth = len(lista)
	pck = listinventory.ListInventory(length)

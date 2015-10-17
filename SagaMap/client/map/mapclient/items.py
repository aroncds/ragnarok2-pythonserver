from packet import Packet
from packets.map.items.set import (
	sendzeny, listinventory, listequipment, weaponlist
)


def SendZeny(client):
	pck = sendzeny.SendZeny()
	pck.setZeny(client.char.zeny)
	client.sendPacket(pck)

def SendListInventory(client):
	lista = client.char.inventory.inventory
	length = len(lista)

	pck = listinventory.ListInventory(length)
	pck.setSortType(0)
	pck.setListItens(lista)

	client.sendPacket(pck)

def SendListEquipment(client):
	lista = client.char.inventory.equipment
	pck = listequipment.ListEquipment()
	pck.setEquipList(lista)
	client.sendPacket(pck)

def SendWeaponList(client):
	pck = weaponlist.WeaponList()
	pck.setWeapons(client.char.weapons)
	client.sendPacket(pck)

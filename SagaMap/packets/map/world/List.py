from packet import Packet
from client.map.mapclient import (
	OnSendMapLoaded, OnDiveUP, OnMoveStart
)
from packets.map.world.get import move_start

dict_packets = {
	0x0301:{
		'function': OnSendMapLoaded,
		'class': Packet,
	},
	0x030A:{
		'function': OnDiveUP,
		'class': Packet
	},
	0x0302:{
		'function': OnMoveStart,
		'class': move_start.MoveStart
	}
}
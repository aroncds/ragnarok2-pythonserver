from packet import Packet
from client.map.mapclient import OnSendMapLoaded, OnDiveUP

dict_packets = {
	0x0301:{
		'function': OnSendMapLoaded,
		'class': Packet,
	},
	0x030A:{
		'function': OnDiveUP,
		'class': Packet
	}
}
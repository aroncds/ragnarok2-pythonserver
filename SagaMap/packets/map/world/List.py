from packet import Packet
from client.map.mapclient import MapClient

dict_packets = {
	0x0301:{
		'function': MapClient.OnSendMapLoaded,
		'class': Packet,
	}	
}
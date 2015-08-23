from Packet import Packet
from Client.Map.MapClient import MapClient

dict_packets = {
	0x0301:{
		'function': MapClient.OnSendMapLoaded,
		'class': Packet,
	}	
}
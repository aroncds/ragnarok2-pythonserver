from packets.map.gateway.identify import GatewayIdentify
from packets.map.world import List as WorldList

from packet import Packet

from client.map.mapclient import MapClient


dict_packets = {
	0x010C:{
		'function': MapClient.OnIdentify,
		'class': GatewayIdentify,
	},
}

dict_packets.update(WorldList.dict_packets)
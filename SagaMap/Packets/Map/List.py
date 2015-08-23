from Packet import Packet

from Client.Map.MapClient import MapClient

from Packets.Map.Gateway.Identify import GatewayIdentify
from Packets.Map.World import List as WorldList

dict_packets = {
	0x010C:{
		'function': MapClient.OnIdentify,
		'class': GatewayIdentify,
	},
}

dict_packets.update(WorldList.dict_packets)
from packets.login.get import (
	sendkey, identanswer
)
from packet import Packet

from client.login.loginmanager import (
	OnSendKey, OnIdentify, OnMapPing, OnIdentAnswer
)

dict_packet = {
	0x0201: {
		'function': OnSendKey,
		'class': sendkey.SendKey
	},
	0x0202:{
		'function': OnIdentify,
		'class': Packet
	},
	0xFE01:{
		'function': OnMapPing,
		'class': Packet
	},
	0xFF01:{
		'function': OnIdentAnswer,
		'class': identanswer.IdentAnswer
	}
}
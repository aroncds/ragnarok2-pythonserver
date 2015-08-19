from Packets.Login.Get import (
	SendKey, IdentAnswer
)

from Packet import Packet
from LoginManager import *

dict_packet = {
	0x0201: {
		'function': OnSendKey,
		'class': SendKey.SendKey
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
		'class': IdentAnswer.IdentAnswer
	}
}
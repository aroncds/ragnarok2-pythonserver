import encryption
import settings

from decorators.packets import onpacket
from packet import Packet
from packets.login.set import (
    sendkey, identify, mappong
)

StaticKey = [
    0x40, 0x21, 0xBF, 0xE4, 0xB0, 0xC7, 0xB8, 0xF0,
    0xB8, 0xA3, 0xB0, 0xDA, 0xC1, 0xF6, 0x24, 0x00
]


@onpacket(sendkey.SendKey, 0x0201)
def OnSendKey(client, data):
    key = data.getKey()
    serverPck = sendkey.SendKey()
    serverPck.setKey(encryption.GenerateDecExpKey(StaticKey))
    serverPck.setColumn(4)
    serverPck.setRounds(10)
    serverPck.setDirection(2)
    client.sendpacket(serverPck)


@onpacket(Packet, 0x0202)
def OnIdentify(client, data):
    pck = identify.Identify()
    pck.setLoginPassword(settings.LOGIN_PASSWORD)
    pck.setWorldName(settings.WORLD_NAME)
    pck.setHostedMaps(settings.HOSTED_MAPS)
    pck.setIP(settings.HOST)
    pck.setPort(settings.PORT)
    client.sendpacket(pck)


@onpacket(Packet, 0xFE01)
def OnMapPing(client, data):
    pck = mappong.MapPong()
    pck.setSessionID(client.sessionID)
    client.sendpacket(pck)


@onpacket(Packet, 0xFF01)
def OnIdentAnswer(client, data):
    erro = data.getError()

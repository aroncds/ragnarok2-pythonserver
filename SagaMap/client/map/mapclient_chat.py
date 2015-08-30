from packets.map.chat.set import sendchat

def SendChatRed(client, message):
	pck = sendchat.SendChat()
	pck.setTypeMessage(0)
	pck.setName(client.char.name)
	pck.setMessage(message)
	client.sendPacket(pck)
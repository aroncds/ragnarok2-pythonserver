from packets.map.skill.set import battleskill, livingskill


def SendListSkill(client):
	skills = client.char.skills
	length = len(skills.battleskills)
	pck = battleskill.BattleSkill(length)
	pck.setSkills(skills.battleskills)
	client.sendpacket(pck)

	# length = len(skills.livingskills)
	# pck = livingskill.LivingSkill()
	# pck.setSkills(skills.livingskills)

	# client.sendPacket(pck)

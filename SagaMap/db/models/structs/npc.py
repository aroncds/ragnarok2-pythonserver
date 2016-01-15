# -*- coding: utf-8 -*-


class Npc:
	__slots__ = [
		'ID' ,'Name' ,'HP' ,'SP' ,'Level' ,'CEXP' ,'JEXP' ,'WEXP' ,'Def' ,
		'Flee' ,'AtkMin' ,'Cri' ,'Hit' ,'ASPD' ,'SightRange' ,'Size' ,
		'WalkSpeed' ,'RunSpeed' ,'LivingSpace'
	]

	def __init__(self, *args, **kwargs):
		for key, item in kwargs.items():
			setattr(self, key, item)
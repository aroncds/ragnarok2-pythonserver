# -*- coding: utf-8 -*-

import pickle
from redis import Redis
from settings import REDIS_CONF
from xml.etree import ElementTree
from db.model import ModelMixin


class ManagerRedis(object):

	def __init__(self):
		self._conn = Redis(db=self.Meta.db, **REDIS_CONF)

	def __getitem__(self, key, val=None):
		value = self._conn.get(key)

		if value:
			get_values = pickle.loads(value)
			instance = self.Meta.model(**get_values)
			return instance
		return val

	get = __getitem__

	def __setitem__(self, key, value):
		if value is dict:
			value = pickle.dumps(value)
			self._conn.set(key, value)
		else:
			raise Exception("Não é possível setar o valor")


class ManagerMixin(object, metaclass=ModelMixin):

	def __init__(self):
		self.created = self._conn.get(self.Meta.name)
		if not self.created:
			self.load_to_redis(self.Meta.dir_data)

	def _create_item(self, instance, values):
		for key, item in values.items():
			if key in self.fields:
				setattr(instance, key, item)

	def load_to_redis(self, src):
		pipe = self._conn.pipeline()

		et = ElementTree.parse(src)
		root = et.getroot()
		lista = root.getchildren()

		for item in lista:
			valuesXML = item.getchildren()
			values = self.__create_dict_item(valuesXML)
			pipe.set(values[self.Meta.key], pickle.dumps(values))

		pipe.set(self.Meta.name, True)
		pipe.execute()

	def __create_dict_item(self, fields):
		item = {}
		for field in fields:
			if field.tag in self.fields:
				item[field.tag] = self.fields[field.tag].convert(field.text)
		return item

class Manager(ManagerRedis, ManagerMixin):
	def __init__(self):
		super().__init__()

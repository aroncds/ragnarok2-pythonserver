# -*- coding: utf-8 -*-
from db.connection import db_connection


class Field(object):
	null=False
	blank=False
	auto_increment=False
	type_field = 'char'
	_field_db = True


class CharField(Field):
	max_length = 50
	type_field = 'char'


class IntField(Field):
	type_field = 'int'


class FloatField(Field):
	type_field = 'float'


class AutoID(IntField):
	auto_increment = True


class Model(object):
	table = ''
	fields = {}
	primary_key = ''

	def __init__(self):
		self.__empty_instance()

	def save(self, connection=None):
		query = self.__update__()
		db_connection.query(query)

	def __empty_instance(self):
		lista= dir(self)
		for key in lista:
			prop = getattr(self, key, None)
			if(hasattr(prop, '_field_db')):
				self.fields[key] = prop
				setattr(self, key, None)

	def get_pk(self):
		if(hasattr(self, self.primary_key)):
			return getattr(self, self.primary_key, None)
		return None

	def select_self(self):
		if self.__self_select__():
			return True

	def __query__select(self):
		id = self.get_pk()
		return "SELECT * FROM `%s` WHERE `%s`=%s" % (
			self.table,
			self.primary_key,
			id
		)

	def __self_select__(self):
		import time
		start_time = time.clock()
		query = self.__query__select()
		result = db_connection.query(query).fetchone()

		for key, item in result.items():
			if(hasattr(self, key)):
				setattr(self, key, item)

		end_time = time.clock() - start_time
		print("Time: " + str(end_time))
		return True

	def __insert__(self):
		fields = []
		values = []

		for key in self.fields.keys():
			v = getattr(self, key, '')
			fields.append("`%s`," % key)
			values.append("'%s'," % v)

		fields = "".join(fields)[:-1]
		values = "".join(values)[:-1]

		return "INSERT INTO `%s` (%s) VALUES (%s);" % (
			self.table,
			fields,
			values
		)

	def __update__(self):
		fields = []

		for key in self.fields.keys():
			v = getattr(self, key, '')
			fields.append(" `%s`='%s'," % (keysey, v))

		fields = "".join(fields)[:-1]
		return "UPDATE `%s` SET%s WHERE id='%s';" % (
			self.table,
			fields,
			self.pk
		)
		
	def delete(self):
		query = "DELETE FROM " + self.table + " WHERE id='%s'" % self.pk


class RelatedModel(object):
	dst_model = None
	src_model = None

	def __init__(self, model, **kwargs):
		self.dst_model = model

		if("related_name" in kwargs):
			setattr(
				self.dst_model,
				kwargs.get('related_name'),
				ManagerModel(model)
			)

	def set_src_model(self, model):
		pass


class ManagerModel(object):
	_model = None

	def __init__(self, model):
		self._model = model


	def filter(self, **kwargs):
		results = []
		query = self.__query__filter__(**kwargs)
		result = db_connection.query(query).fetchall()

		for item in result:
			model = self._model()
			for key, value in item:
				if(hasattr(model, key)):
					setattr(model, key, value)

	def __related_model__(self):
		pass

	def __query__filter__(self, **kwargs):
		table = self._model.table
		lista = []
		for key, item in kwargs:
			lista.append("`%s`='%s' AND " % (key, item))
		prop = "".join(lista)[:-5]
		return "SELECT * FROM `%s` WHERE %s" % (table, prop) 

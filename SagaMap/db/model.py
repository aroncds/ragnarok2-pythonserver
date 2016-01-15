ga# -*- coding: utf-8 -*-
from db.connection import db_connection
import struct


class Field(object):
	null=False
	blank=False
	auto_increment=False
	type_field = 'varchar'
	_field_db = True

	def convert(self, value):
		pass


class CharField(Field):
	max_length = 50
	type_field = 'varchar'

	def convert(self, value):
		return str(value)


class IntField(Field):
	type_field = 'int'

	def convert(self, value):
		return int(value)


class FloatField(Field):
	type_field = 'float'

	def convert(self, value):
		return float(value)


class ByteArrayField(Field):
	type_field = 'byte'

	def convert(self, value):
		length = int(len(value) / 2)

		b = [0] * (length);

		for i in range(length):
			index = i * 2
			b[i] = struct.unpack(
				'b',
				bytes.fromhex(value[index:index+2])
			)[0]

		return b


class ListIntField(Field):
	type_field = 'char'

	def convert(self, value):
		values = value.split(",")
		lista = [int(val) for val in values]
		return lista


class AutoID(IntField):
	auto_increment = True


class RelatedModel(object):
	dst_model = None
	src_model = None

	def __init__(self, model, **kwargs):
		self.dst_model = model

		if "related_name" in kwargs:
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
			model.set_values(item)
			results.append(model)

		return results

	def __related_model__(self):
		pass

	def __query__filter__(self, **kwargs):
		table = self._model.table
		lista = []
		for key, item in kwargs.items():
			lista.append("`%s`='%s' AND " % (key, item))
		prop = "".join(lista)[:-4]
		return "SELECT * FROM `%s` WHERE %s" % (table, prop) 


class ModelMixin(type):

	def __init__(self, *args, **kwargs):
		self.__construct_fields()
		self.objects = ManagerModel(self)
		super(ModelMixin, self).__init__(*args, **kwargs)

	def __construct_fields(self):
		if getattr(self, 'fields', None):
			return None
		self.fields = {}
		lista= dir(self)
		for key in lista:
			prop = getattr(self, key, None)
			if hasattr(prop, '_field_db'):
				self.fields[key] = prop
				setattr(self, key, None)


class SQLCompiler(object):
	def __query__select(self):
		return "SELECT * FROM `%s` WHERE `%s`=%s" % (
			self.table,
			self.primary_key,
			self.pk
		)

	def __self_select__(self):
		query = self.__query__select()
		result = db_connection.query(query).fetchone()
		self.set_values(result)
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
			fields.append(" `%s`='%s'," % (key, v))

		fields = "".join(fields)[:-1]
		return "UPDATE `%s` SET%s WHERE id='%s';" % (
			self.table,
			fields,
			self.pk
		)


class Model(SQLCompiler, metaclass=ModelMixin):
	table = ''
	primary_key = ''

	@property
	def pk(self):
		if hasattr(self, self.primary_key):
			return getattr(self, self.primary_key, None)

	def save(self, connection=None):
		query = self.__update__()
		db_connection.query(query)

	def select_self(self):
		if self.__self_select__():
			return True
		
	def delete(self):
		query = "DELETE FROM " + self.table + " WHERE id='%s'" % self.pk

	def set_values(self, result):
		if hasattr(result, 'items'):
			for key, item in result.items():
				if(hasattr(self, key) and key in self.fields):
					setattr(self, key, self.fields[key].convert(item))


class ModelXML(metaclass=ModelMixin):
	
	def set_values(self, fields):
		for field in fields:
			if hasattr(self, field.tag):
				setattr(
					self,
					field.tag,
					self.fields[field.tag].convert(field.text)
				)

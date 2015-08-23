from DB.connection import db_connection

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
	pk = Field
	table = 'Char'
	fields = {}

	def __init__(self):
		self.__empty_instance()

	def save(self, connection=None):
		query = self.__update__()
		db_connection.query(query)
		import ipdb; ipdb.set_trace()
		print "Hehe"

	def __empty_instance(self):
		lista= dir(self)
		for key in lista:
			prop = getattr(self, key, None)
			if(hasattr(prop, '_field_db')):
				self.fields[key] = prop
				setattr(self, key, None)

	def __query__select(self):
		query = "SELECT * FROM WHERE id=%s"

	def __insert__(self):
		fields = []
		values = []

		for key in self.fields.keys():
			v = getattr(self, key, '')
			fields.append("`%s`," % key)
			values.append("'%s'," % v)

		fields = "".join(fields)[:-1]
		values = "".join(values)[:-1]

		return "INSERT INTO " + self.table + " (%s) VALUES (%s);" % (fields, values)

	def __update__(self):
		fields = []

		for key in self.fields.keys():
			v = getattr(self, key, '')
			fields.append(" `%s`='%s'," % (key, v))

		fields = "".join(fields)[:-1]

		query = "UPDATE " + self.table + " SET %s WHERE id='%s';" % (fields, self.pk)
		return query
		

	def delete(self):
		query = "DELETE FROM " + self.table + " WHERE id='%s'" % self.pk
		
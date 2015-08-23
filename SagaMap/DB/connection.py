# -*- coding: utf-8 -*-
import pymysql.cursors

from settings import DATABASE
from pymysql.err import *


class Connection(object):
	conn = None
	def __init__(self, host, user, password, port, dbname):
		try:
			self.conn = pymysql.connect(
				host=host,
				user=user,
				password=password,
				db=dbname,
				port=port,
				cursorclass=pymysql.cursors.DictCursor,
				)
		except MySQLError as e:
			raise BaseException(e)


	def query(self, qry):
		result = None
		try:
			with self.conn.cursor() as cursor:
				if cursor.execute(qry):
					result = cursor
		except MySQLError as e:
			raise BaseException(e)

		return result


db_connection = Connection(
	DATABASE['default']['HOST'],
	DATABASE['default']['USER'],
	DATABASE['default']['PASSWORD'],
	DATABASE['default']['PORT'],
	DATABASE['default']['DBNAME']
)

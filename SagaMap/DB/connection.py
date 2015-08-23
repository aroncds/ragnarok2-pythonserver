from settings import DATABASE
from pymysql.err import *
import pymysql.cursors


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
				)
		except:
			raise BaseException("Erro")


	def query(self, qry):
		result = None
		try:
			with self.conn.cursor() as cursor:
				cursor.execute(qry)
				result = cursor.fetchall()
		except MySQLError as e:
			print e


db_connection = Connection(
	DATABASE['default']['HOST'],
	DATABASE['default']['USER'],
	DATABASE['default']['PASSWORD'],
	DATABASE['default']['PORT'],
	DATABASE['default']['DBNAME']
)
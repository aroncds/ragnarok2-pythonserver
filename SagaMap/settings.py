HOST = "127.0.0.1"
PORT = 3011

LOGIN_HOST = "127.0.0.1"
LOGIN_PORT = 6000

LOGIN_PASSWORD = "secret"

WORLD_NAME = "Saga1"

DATABASE = {
	"default": {
		"HOST": "127.0.0.1",
		"USER": "root",
		"PASSWORD": "admin",
		"PORT": 3306,
		"DBNAME": "ro2"
	}
}

HOSTED_MAPS = [
	1,2,3,4,5,6,7,8,9,10,11,12,13,14,
	15,16,17,18,19,20,21,22,23,24,25,26,
]

DIRECTORY_DB = "/home/aron/projetos/serverro2/DB/"

ITEM_DB = "DB.xml"

try:
	from .local_settings import *
except:
	pass
import time
from packets import packets

def onpacket(func, packet, id):
	packets[id] = {'func': func, 'class': packet}

	def inner (*args, **kwargs):
		return func(*args, **kwargs)

	return inner

def check_time(func):
	def inner(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		stop = time.time() - start
		print(func.__name__ + " - %s " % stop)
		return result

	return inner

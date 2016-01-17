import time
from packets import packets

def onpacket(packet, id):
	def decorator(func):
		packets[id] = {'func': func, 'class': packet}
		def inner (*args, **kwargs):
			return func(*args, **kwargs)
		return inner
	return decorator


def check_time(func):
	def inner(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		stop = time.time() - start
		print(func.__name__ + " - %s " % stop)
		return result

	return inner

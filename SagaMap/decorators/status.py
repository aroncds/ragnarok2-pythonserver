def maploaded(func):
	def inner(*args, **kwargs):
		client = kwargs.get("client", None)
		print(hasattr(client, 'char'))
		if (hasattr(client, 'char')):
			func(client)
	return inner
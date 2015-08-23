def MapLoaded(func):
	def test_char(client):
		print(hasattr(client, 'char'))
		if (hasattr(client, 'char')):
			func(client)
	return test_char
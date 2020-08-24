import json

class User():

	def __init__(self, login, name, phone):
		self.login = login
		self.name  = name
		self.phone = phone

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
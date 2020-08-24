import json

class UserError():

	def __init__(self, message):
		self.message = message

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
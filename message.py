from user import User
from user_error import UserError

class Message():

	def handle_message(self, message):
	    #robsonagapito;Robson Agapito;11986613181
	    mens = str(message)
	    mens = mens[2:-1]
	    mens = mens.split(";")
	    if (len(mens) == 3):
	        user = User(mens[0], mens[1], mens[2])
	        return user.toJSON()
	    else:
	        userError = UserError("Fields qtty is lower than 3!")
	        return  userError.toJSON()
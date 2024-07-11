from enum import Enum
from pydantic import BaseModel

class Admin():
	def currentuser():
		login = True
		return login

class Account(BaseModel):
	name:str |  None
	# print("Name :",name)
	id:int
	email:str


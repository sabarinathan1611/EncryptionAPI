from enum import Enum
from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class Admin():
	def currentuser():
		login = True
		return login

class Account(BaseModel):
    name: Optional[str]
    id: int
    email: str

    @validator('email')
    def email_validation(cls, value):
        if '@' not in value:
            raise ValueError("Invalid Email Address")
        return value


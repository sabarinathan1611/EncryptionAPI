from pydantic import BaseModel

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:str or None =None
    
class User(BaseModel):
    username:str or None =None
    email:str or None =None 
    disable:bool or None = None 

class UserInDB(User):
    hash_password:str
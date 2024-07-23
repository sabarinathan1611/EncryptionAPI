from fastapi import Depends,status,HTTPException
from datetime import datetime ,timedelta
from jose import JWTError , jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from .Model import *
from .DB  import *

SECRETKEY="4354unwgergy34t3983rbd9w4t*#@"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_TIME = 5

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_2_scheme=OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password,hash_password):
    return pwd_context.verify(plain_password,hash_password)

def get_hash_password(password):
    
    return pwd_context.hash(password)

def get_user(db,username:str):
    if username in db:
        userdata=db[username]
        return UserInDB(**userdata)
    
def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRETKEY, algorithm=ALGORITHM)
    return encoded_jwt


def authuser(db,username:str,password:str):
    user=get_user(db,username)
    if not user :
        return False
    if not verify_password(password,user.hash_password):
        return False
    return user


async def get_current_user(token:str=Depends(oauth_2_scheme)):
    credential_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    
    try:
        payload=jwt.decode(token,SECRETKEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username is None:
            raise credential_exception
        token_Data=TokenData(username=username)
        
        
    except JWTError:
        raise credential_exception
        
    user = get_user(db,token_Data.username)
    if user is None:    
        raise credential_exception
    return user 

async def get_current_active_user(current_user:UserInDB=Depends(get_current_user)):
    if current_user.disable:
        raise HTTPException(status_code=400,detail="Inactive User")
    return current_user
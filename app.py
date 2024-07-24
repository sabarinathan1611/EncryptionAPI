from fastapi import Depends , FastAPI,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from Model import *

app =FastAPI()  

@app.post("/token",response_model=Token)
async def login_for_accesss(form_data:OAuth2PasswordRequestForm=Depends()):
    user=authuser(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Username or Password",headers={"WWW-Authenticate":"Bearer"})
    access_token_time=timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    access_token=create_access_token(data={"sub":user.username},expires_delta=access_token_time)   
    return {"access_token": access_token, "token_type": "bearer"}  


@app.get("/user/me/",response_model=User)
async def read_user(current_user:User=Depends(get_current_active_user)):
    return current_user


@app.get("/user/me/items")
async def read_user_items(current_user:User=Depends(get_current_active_user)):
    return [{"item_id":1,"owner":current_user}]
#testt

    
from fastapi import FastAPI,HTTPException
from Model.Model import *
accounts_db = {}

app =FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/parameter')
async def parameter(id:int):
	return {"Given ID :":id }


@app.get('/list')
async def listpath():
	return ['TEST1','TEST2']


@app.get('/model/{name}')
async def model(name:str):
	print("Model.name : ",Model.name())
	print("Name : ",name)


	if name == Model.name():
		user = Admin.currentuser();
		return {"Name :":Model.name(),"JOB :":Model.job(),"Login :":user}
	else:
		return 404


@app.get('/path/{file:path}')
def filepathe(file:str):
	return {"File Path :":file}


@app.post('/account',response_model=Account)
async def creeate_account(account:Account):
	print("account:",account)
	if account.id in accounts_db:
        raise HTTPException(status_code=400, detail="Account with this ID already exists.")
    	accounts_db[account.id] = account
    return account


@app.get('/account/{id}',response_model=Account)
async def getAccount(id):
	account = accounts_db.get(account_id)
	if account is None:
        raise HTTPException(status_code=404, detail="Account not found.")
    return account



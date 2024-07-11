from fastapi import FastAPI
from Model.Model import *


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


@app.post('/account')
async def account(acc:Account):
	print(acc.name)
	return acc


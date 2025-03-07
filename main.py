from fastapi import FastAPI, File, UploadFile, Request, Response
from pydantic import BaseModel
import time

class User(BaseModel):
    name : str
    roll : str
    id : str

app = FastAPI()


users = [
    User(id="1", name="Utsav", roll="23"),
    User(id="2", name="Kaushal", roll="24"),
    User(id="3", name="Smit", roll="25")
]


class UserService:
    
    def addUser(self, user : User):
        users.append(user)

service = UserService()

@app.get("/")
def home():
    return {"message" : "This is FastApi Server."}

@app.post("/sum")
def sum(a : int, b : int):
    sum = a + b
    return {"message" : f"The sum for given values is {sum}"}

@app.post("/substract")
def substract(a : int, b : int):
    sub = a - b
    return {
        "message" : f"The substraction of given values will be {sub}"
    }

@app.post("/user")
def create_user(user : User):
    print("userId: ", user.id)
    service.addUser(user)

    return users

@app.post("/upload-file")
def upload_file(file : UploadFile):
    return {"filename " : file}

@app.middleware('log-request-timings')
async def log_reqt(request : Request, callnxt):

    print("middleware 1")

    body = await request.body()
    params = request.query_params
    

    print("body : ", body)
    print("params : ", params)
    print("headers : ", request.headers)
    startTime = time.time()


    response = await callnxt(request)
    endTime = time.time()

    duration = endTime - startTime

    log = {
        "request" : request.url,
        "duration" : duration,
    }

    print("Request Log : ", log)

    return response


@app.middleware('practice-mid')
async def practice_mid(request : Request, callnxt):

    print("middleware 2")
    response = await callnxt(request)

    return response
    


from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from model import MobileNetImplementation

class RequestBody(BaseModel):
    url:str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"hello worlds this is something to connect stuff"}

@app.put("/predict")
def predict(content:RequestBody):
    
    return {"result": "unprepared"}
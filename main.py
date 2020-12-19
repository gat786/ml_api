from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
    model = MobileNetImplementation()
    result = model.predict_image(content.url)
    return JSONResponse(content=result)
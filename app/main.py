from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .model import MobileNetImplementation

class RequestBody(BaseModel):
    url:str

app = FastAPI()
model = MobileNetImplementation()

@app.get("/")
def read_root():
    return {"message":"hello worlds this is something to connect stuff"}

@app.put("/predict")
def predict(content:RequestBody):
    result = model.predict_image(content.url)
    if result:
        return JSONResponse(content=result)
    else:
        raise  HTTPException(status_code=404,detail="Not able to load image from url")
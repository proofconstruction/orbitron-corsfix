
from neighbor.service import NeighborService

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

service = NeighborService()
service.storage.connect()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/nearest/{count}/{sourceType}/to/{postalCode}")
async def nearest(count: int, sourceType: str, postalCode: str):
    return service.getNearestNeighbor(count, sourceType, postalCode, 1000)

@app.get("/nearest/{count}/{sourceType}/to/{postalCode}/within/{miles}")
async def nearestWithin(count: int, sourceType: str, postalCode: str, miles:int):
    return service.getNearestNeighbor(count, sourceType, postalCode, miles)

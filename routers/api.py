from fastapi import APIRouter
import sys

api = APIRouter(prefix="/api")


@api.get("/hello")
async def hello():
    return "Hello"


@api.get("/platform")
async def platform():
    res = str(sys.version_info)
    return res

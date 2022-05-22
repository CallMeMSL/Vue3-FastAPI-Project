from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

fe = APIRouter()

templates = Jinja2Templates(directory="dist/spa")


@fe.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

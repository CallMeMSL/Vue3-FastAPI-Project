import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routers.api import api
from routers.frontend import fe

app = FastAPI()
app.include_router(api)
try:
    app.mount("/assets", StaticFiles(directory="dist/spa/assets"), name="static")
except RuntimeError:
    app.add_middleware(
        CORSMiddleware,
        allow_origins="http://localhost:9000",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(fe)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

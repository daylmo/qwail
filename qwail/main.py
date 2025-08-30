from fastapi import FastAPI

from qwail import VERSION
from qwail.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    version=VERSION,
)


@app.get("/")
async def index():
    return {"message": "Hello from Qwail!!"}

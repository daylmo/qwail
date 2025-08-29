from fastapi import FastAPI

from qwail.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
)


@app.get("/")
async def index():
    return {"message": "Hello from Qwail!!"}

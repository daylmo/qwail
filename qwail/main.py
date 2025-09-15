from fastapi import FastAPI

from qwail import DESCRIPTION, VERSION
from qwail.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    license_info={
        "name": "MIT License",
        "identifier": "MIT",
    },
)


@app.get("/")
async def main():
    return {"message": "Hello Qwail!!"}

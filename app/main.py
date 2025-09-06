from fastapi import FastAPI

from app import VERSION

app = FastAPI(
    title="Qwail",
    version=VERSION,
)


@app.get("/")
async def main():
    return {"message": "Hello Qwail!!"}

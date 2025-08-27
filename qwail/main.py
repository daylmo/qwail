from fastapi import FastAPI

app = FastAPI(title="Qwail")


@app.get("/")
async def index():
    return {"message": "Hello from Qwail!!"}

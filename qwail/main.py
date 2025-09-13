from fastapi import FastAPI

from qwail import VERSION

app = FastAPI(
    title="qwail",
    version=VERSION,
)

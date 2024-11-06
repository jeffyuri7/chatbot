#!/usr/bin/env python3
from chatbot import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI()

add_routes(app, chain, path="/chatbot")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

from fastapi import FastAPI
from dotenv import load_dotenv

from app.routes import router_api

load_dotenv()

app = FastAPI(title="E-commerce API", version="0.1.0")

app.include_router(router_api)

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    print('teste')
    app.mongodb_client = AsyncIOMotorClient(os.environ["MONGO_URI"])
    app.mongodb = app.mongodb_client[os.environ.get("MONGO_DB_NAME", "meu_banco")]
    print("🔌 MongoDB conectado com sucesso.")
    # EXECUTA ANTES
    yield
    # EXECUTA DEPOIS
    app.mongodb_client.close()
    print("❌ Conexão com MongoDB encerrada.")


app = FastAPI(lifespan=lifespan)

# Rota de exemplo
@app.get("/")
async def root():
    return {"message": "API rodando com FastAPI e MongoDB!"}

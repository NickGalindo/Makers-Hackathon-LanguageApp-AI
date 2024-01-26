from manager.load_config import CONFIG

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

import pymilvus

import colorama 
from colorama import Fore

from sentence_transformers import SentenceTransformer

from vectordb.setupCollections import setupCols
from endpoints import router as endpoints_router

colorama.init(autoreset=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.milvusConnection = pymilvus.connections.connect(
        alias=CONFIG["VDB_ALIAS"],
        host=CONFIG["VDB_HOST"],
        port=CONFIG["VDB_PORT"]
    )

    app.state.fr_card_col, app.state.fr_word_col, app.state.en_card_col, app.state.en_word_col = setupCols()

    app.state.transformerModel = SentenceTransformer(CONFIG["TRANSFORMER_MODEL"])

    yield

    app.state.fr_card_col.flush()
    app.state.fr_word_col.flush()
    app.state.en_card_col.flush()
    app.state.en_word_col.flush()
    app.state.fr_card_col.release()
    app.state.fr_word_col.release()
    app.state.en_card_col.release()
    app.state.en_word_col.release()

    pymilvus.connections.disconnect(CONFIG["VDB_ALIAS"])


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints_router)

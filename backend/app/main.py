from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models  # noqa: F401 - importa modelos para que create_all los detecte
from app.routers import auth, recursos, compartir


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Visualia API", lifespan=lifespan)

app.include_router(auth.router)
app.include_router(auth.router_buscar)
app.include_router(recursos.router)
app.include_router(compartir.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok"}

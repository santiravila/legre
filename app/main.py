from fastapi import FastAPI
from .usuarios.router import router as router_usuarios
from .infra.database import Base, engine
from .common import models

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_usuarios)

@app.post("")
def root():
    pass
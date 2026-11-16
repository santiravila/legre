from fastapi import FastAPI
from usuarios.router import router as router_usuarios
from common import models
from infra.database import engine, Base

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(router_usuarios)

@app.post("")
def root():
    pass
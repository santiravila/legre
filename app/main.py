from fastapi import FastAPI
from usuarios.router import router as router_usuarios

app = FastAPI()
app.include_router(router_usuarios)

@app.post("")
def root():
    pass
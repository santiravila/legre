from .schema import UsuarioCrear, UsuarioRespuesta
from .service import UsuarioServicio
from .repository import UsuarioRepositorio
from common.dependencies import DBSession
from fastapi import APIRouter, Depends
from typing import Annotated


router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

def get_service_dependency(session: DBSession):
    repo = UsuarioRepositorio(session)
    return UsuarioServicio(repo, session)

ServiceDep = Annotated[UsuarioServicio, Depends(get_service_dependency)]

@router.post("", response_model=UsuarioRespuesta)
def crear_usuario(
    payload: UsuarioCrear,
    servicio: ServiceDep
) -> UsuarioRespuesta:  
    usuario = servicio.crear_usuario(payload)
    return UsuarioRespuesta.model_validate(usuario)
from .schema import UsuarioCrear, UsuarioRespuesta, UsuarioActualizar
from .service import UsuarioServicio
from .repository import UsuarioRepositorio
from ..common.dependencies import DBSession
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


@router.get("{user_id}", response_model=UsuarioRespuesta)
def leer_usuario(
    user_id: int,
    servicio: ServiceDep
) -> UsuarioRespuesta:
    usuario = servicio.leer_usuario(user_id)
    return UsuarioRespuesta.model_validate(usuario)


@router.delete("{user_id}", response_model=UsuarioRespuesta)
def eliminar_usuario(
    user_id: int,
    servicio: ServiceDep
) -> UsuarioRespuesta:
    usuario_eliminado = servicio.eliminar_usuario(user_id)
    return UsuarioRespuesta.model_validate(usuario_eliminado)


@router.patch("{user_id}", response_model=UsuarioRespuesta)
def actualizar_usuario(
    user_id: int,
    payload: UsuarioActualizar,
    servicio: ServiceDep
) -> UsuarioRespuesta:
    usuario_actualizado = servicio.actualizar_usuario(user_id, payload)
    return UsuarioRespuesta.model_validate(usuario_actualizado)
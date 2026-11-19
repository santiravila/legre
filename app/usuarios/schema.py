from datetime import datetime
from pydantic import BaseModel, ConfigDict


class UsuarioBase(BaseModel):
    nombre: str
    password: str #temporal


class UsuarioCrear(UsuarioBase):
    pass


class UsuarioRespuesta(UsuarioBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    fecha_registro: datetime


class UsuarioActualizar(UsuarioBase):
    nombre: str | None = None
    password: str | None = None

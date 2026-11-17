from .schema import UsuarioCrear
from .models import Usuario
from .repository import UsuarioRepositorio
from sqlalchemy.orm import Session


class UsuarioServicio:
    def __init__(
            self, 
            repo: UsuarioRepositorio, 
            session: Session
        ) -> None:
        self.repo = repo #proteger
        self.session = session

    def crear_usuario(self, payload: UsuarioCrear) -> Usuario:
        try:
            nuevo_usuario = Usuario(
                nombre = payload.nombre,
                password = payload.password
            )

            usuario_db = self.repo.guardar_usuario(nuevo_usuario)
            self.session.commit()
            return usuario_db
        except Exception:
            self.session.rollback()
            raise

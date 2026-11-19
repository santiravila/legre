from .schema import UsuarioCrear, UsuarioActualizar
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

    def leer_usuario(self, user_id: int):
        try:
            usuario_db = self.repo.cargar_usuario(user_id=user_id)
            self.session.commit()
            return usuario_db
        except Exception:
            self.session.rollback()
            raise

    def eliminar_usuario(self, user_id: int):
        try:
            usuario = self.leer_usuario(user_id=user_id)
            usuario_db = self.repo.borrar_usuario(usuario)
            self.session.commit()
            return usuario_db
        except Exception:
            self.session.rollback()
            raise

    def actualizar_usuario(self, user_id: int, payload: UsuarioActualizar):
        try:
            update_fields = payload.model_dump(exclude_unset=True)
            usuario = self.leer_usuario(user_id=user_id)

            for key, value in update_fields.items():
                setattr(usuario, key, value)

            self.session.commit()
            return usuario
        except Exception:
            self.session.rollback()
            raise

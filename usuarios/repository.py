from .models import Usuario
from sqlalchemy.orm import Session

class UsuarioRepositorio:
    def __init__(
        self,
        session: Session    
            ) -> None:
        self.session = session


    def guardar_usuario(self, usuario: Usuario) -> Usuario:
        self.session.add(usuario)
        self.session.flush()
        self.session.refresh(usuario)

        return usuario
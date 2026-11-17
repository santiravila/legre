from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from ..infra.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha_registro: Mapped[datetime] = mapped_column(default=datetime.now)
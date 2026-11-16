from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings


engine = create_engine(
    url=settings.DATABASE_URL
)


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine)


def get_db_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()

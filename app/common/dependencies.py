from ..infra.database import get_db_session
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session


DBSession = Annotated[Session, Depends(get_db_session)]
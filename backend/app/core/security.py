import uuid
from typing import Annotated
from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.database import get_db
from app.models import Docente, Sesion

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def generate_token() -> str:
    return str(uuid.uuid4())


def obtener_docente_actual(
    authorization: Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db)
) -> Docente:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token no proporcionado")

    token = authorization.replace("Bearer ", "")
    sesion = db.query(Sesion).filter(Sesion.token == token).first()

    if not sesion:
        raise HTTPException(status_code=401, detail="Token invalido")

    docente = db.query(Docente).filter(Docente.id == sesion.docente_id).first()
    if not docente:
        raise HTTPException(status_code=401, detail="Docente no encontrado")

    return docente


DocenteActualDep = Annotated[Docente, Depends(obtener_docente_actual)]

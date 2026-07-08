from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Docente, Sesion
from app.core.security import (
    hash_password, verify_password, generate_token, DocenteActualDep
)
from app.schemas import (
    DocenteCreate, DocenteResponse,
    SesionCreate, SesionResponse,
    DocenteBusqueda
)

router = APIRouter(prefix="/auth", tags=["auth"])

DBDep = Annotated[Session, Depends(get_db)]


@router.post("/registro", response_model=SesionResponse)
def registro(docente_data: DocenteCreate, db: DBDep):
    existing = db.query(Docente).filter(Docente.nombre == docente_data.nombre).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Ese nombre ya esta en uso, prueba con otro, por ejemplo agregando tu inicial de apellido"
        )

    docente = Docente(
        nombre=docente_data.nombre,
        password_hash=hash_password(docente_data.password)
    )
    db.add(docente)
    db.commit()
    db.refresh(docente)

    sesion = Sesion(
        docente_id=docente.id,
        token=generate_token()
    )
    db.add(sesion)
    db.commit()
    db.refresh(sesion)
    return sesion


@router.post("/login", response_model=SesionResponse)
def login(login_data: SesionCreate, db: DBDep):
    docente = db.query(Docente).filter(Docente.nombre == login_data.nombre).first()

    if not docente or not verify_password(login_data.password, docente.password_hash):
        raise HTTPException(status_code=401, detail="Nombre o password incorrectos")

    sesion = Sesion(
        docente_id=docente.id,
        token=generate_token()
    )
    db.add(sesion)
    db.commit()
    db.refresh(sesion)
    return sesion


@router.post("/logout")
def logout(
    db: DBDep,
    docente: DocenteActualDep,
    authorization: Annotated[str | None, Header()] = None,
):
    token = authorization.replace("Bearer ", "")
    sesion = db.query(Sesion).filter(Sesion.token == token).first()
    if sesion:
        db.delete(sesion)
        db.commit()
    return {"mensaje": "Sesion cerrada correctamente"}


router_buscar = APIRouter(prefix="/docentes", tags=["docentes"])


@router_buscar.get("/buscar", response_model=list[DocenteBusqueda])
def buscar_docentes(
    q: str,
    docente_actual: DocenteActualDep,
    db: DBDep
):
    docentes = db.query(Docente).filter(
        Docente.nombre.ilike(f"%{q}%"),
        Docente.id != docente_actual.id
    ).all()
    return docentes

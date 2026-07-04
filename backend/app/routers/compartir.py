from typing import Annotated
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.models import Recurso, RecursoCompartido, EnlacePublico, Docente
from app.core.security import DocenteActualDep
from app.schemas import CompartirResponse, EnlacePublicoResponse

router = APIRouter(tags=["compartir"])

DBDep = Annotated[Session, Depends(get_db)]


@router.post("/recursos/{recurso_id}/compartir-con-docente", response_model=CompartirResponse)
def compartir_con_docente(
    recurso_id: int,
    docente_destino_id: int,
    docente: DocenteActualDep,
    db: DBDep
):
    # Verificar que el recurso existe y es del docente actual
    recurso = db.execute(
        select(Recurso).where(Recurso.id == recurso_id)
    ).scalar_one_or_none()

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    if recurso.docente_id != docente.id:
        raise HTTPException(
            status_code=403,
            detail="Solo el dueño original puede compartir el recurso"
        )

    # Verificar que el docente destino existe
    docente_destino = db.execute(
        select(Docente).where(Docente.id == docente_destino_id)
    ).scalar_one_or_none()

    if not docente_destino:
        raise HTTPException(status_code=404, detail="Docente destino no encontrado")

    if docente_destino_id == docente.id:
        raise HTTPException(
            status_code=400,
            detail="No puedes compartir un recurso contigo mismo"
        )

    # Verificar si ya existe la compartición
    compartido_existente = db.execute(
        select(RecursoCompartido).where(
            RecursoCompartido.recurso_id == recurso_id,
            RecursoCompartido.compartido_por_id == docente.id,
            RecursoCompartido.compartido_con_id == docente_destino_id
        )
    ).scalar_one_or_none()

    if compartido_existente:
        return compartido_existente

    # Crear la compartición
    nueva_comparticion = RecursoCompartido(
        recurso_id=recurso_id,
        compartido_por_id=docente.id,
        compartido_con_id=docente_destino_id
    )
    db.add(nueva_comparticion)
    db.commit()
    db.refresh(nueva_comparticion)

    return nueva_comparticion


@router.post("/recursos/{recurso_id}/enlace-publico", response_model=EnlacePublicoResponse)
def crear_enlace_publico(
    recurso_id: int,
    docente: DocenteActualDep,
    db: DBDep
):
    # Verificar que el recurso existe y es del docente actual
    recurso = db.execute(
        select(Recurso).where(Recurso.id == recurso_id)
    ).scalar_one_or_none()

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    if recurso.docente_id != docente.id:
        raise HTTPException(
            status_code=403,
            detail="Solo el dueño original puede crear enlaces públicos"
        )

    # Verificar si ya existe un enlace
    enlace_existente = db.execute(
        select(EnlacePublico).where(EnlacePublico.recurso_id == recurso_id)
    ).scalar_one_or_none()

    if enlace_existente:
        return enlace_existente

    # Crear nuevo enlace
    nuevo_enlace = EnlacePublico(
        recurso_id=recurso_id,
        token=str(uuid.uuid4())
    )
    db.add(nuevo_enlace)
    db.commit()
    db.refresh(nuevo_enlace)

    return nuevo_enlace


@router.get("/compartido/{token}")
def ver_recurso_publico(token: str, db: DBDep):
    # Buscar el enlace
    enlace = db.execute(
        select(EnlacePublico).where(EnlacePublico.token == token)
    ).scalar_one_or_none()

    if not enlace:
        raise HTTPException(status_code=404, detail="Enlace no válido")

    # Buscar el recurso
    recurso = db.execute(
        select(Recurso).where(Recurso.id == enlace.recurso_id)
    ).scalar_one_or_none()

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    return {
        "id": recurso.id,
        "tipo": recurso.tipo,
        "titulo": recurso.titulo,
        "html_content": recurso.html_content,
        "creado_en": recurso.creado_en
    }

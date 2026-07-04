from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Recurso
from app.core.security import DocenteActualDep
from app.schemas import RecursoCreate, RecursoResponse
from app.services.gemini_client import gemini_client
from app.services.prompt_builder import construir_prompt
from app.services.seguridad_contenido import validar_html

router = APIRouter(prefix="/recursos", tags=["recursos"])

DBDep = Annotated[Session, Depends(get_db)]


@router.post("/generar", response_model=RecursoResponse)
def generar_recurso(
    recurso_data: RecursoCreate,
    docente: DocenteActualDep,
    db: DBDep
):
    prompt = construir_prompt(
        tipo=recurso_data.tipo,
        prompt_usuario=recurso_data.prompt_usuario,
        modo_proyeccion=recurso_data.modo_proyeccion
    )

    html_content = gemini_client.generate_content(prompt)

    html_content = validar_html(html_content)

    recurso = Recurso(
        docente_id=docente.id,
        tipo=recurso_data.tipo,
        titulo=recurso_data.titulo,
        prompt_usuario=recurso_data.prompt_usuario,
        modo_proyeccion=recurso_data.modo_proyeccion,
        html_content=html_content
    )
    db.add(recurso)
    db.commit()
    db.refresh(recurso)

    return recurso

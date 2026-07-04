from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import select, literal_column, text
from app.database import get_db
from app.models import Recurso, RecursoCompartido, Favorito, Docente
from app.core.security import DocenteActualDep
from app.schemas import RecursoCreate, RecursoResponse, RecursoConOrigen
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


@router.get("/mis-recursos", response_model=list[RecursoConOrigen])
def mis_recursos(
    docente: DocenteActualDep,
    db: DBDep,
    tipo: str | None = Query(None, description="Filtrar por tipo: ficha, hoja_grafica, afiche, lamina"),
    es_favorito: bool | None = Query(None, description="Filtrar solo favoritos")
):
    todos_recursos = []

    # Propios
    result_propios = db.execute(
        select(Recurso, text("'propio' as origen"))
        .where(Recurso.docente_id == docente.id)
    ).all()

    for recurso, origen in result_propios:
        favorito = db.execute(
            select(Favorito).where(
                Favorito.docente_id == docente.id,
                Favorito.recurso_id == recurso.id
            )
        ).first()

        todos_recursos.append(RecursoConOrigen(
            id=recurso.id,
            docente_id=recurso.docente_id,
            tipo=recurso.tipo,
            titulo=recurso.titulo,
            prompt_usuario=recurso.prompt_usuario,
            modo_proyeccion=recurso.modo_proyeccion,
            html_content=recurso.html_content,
            creado_en=recurso.creado_en,
            origen="propio",
            compartido_por=None,
            es_favorito=favorito is not None
        ))

    # Compartidos conmigo
    result_compartidos = db.execute(
        select(Recurso, Docente.nombre.label("compartido_por"), text("'compartido' as origen"))
        .join(RecursoCompartido, Recurso.id == RecursoCompartido.recurso_id)
        .join(Docente, RecursoCompartido.compartido_por_id == Docente.id)
        .where(RecursoCompartido.compartido_con_id == docente.id)
    ).all()

    for recurso, compartido_por, origen in result_compartidos:
        favorito = db.execute(
            select(Favorito).where(
                Favorito.docente_id == docente.id,
                Favorito.recurso_id == recurso.id
            )
        ).first()

        todos_recursos.append(RecursoConOrigen(
            id=recurso.id,
            docente_id=recurso.docente_id,
            tipo=recurso.tipo,
            titulo=recurso.titulo,
            prompt_usuario=recurso.prompt_usuario,
            modo_proyeccion=recurso.modo_proyeccion,
            html_content=recurso.html_content,
            creado_en=recurso.creado_en,
            origen="compartido",
            compartido_por=compartido_por,
            es_favorito=favorito is not None
        ))

    # Filtros
    if tipo:
        todos_recursos = [r for r in todos_recursos if r.tipo == tipo]
    if es_favorito is True:
        todos_recursos = [r for r in todos_recursos if r.es_favorito]

    todos_recursos.sort(key=lambda x: x.creado_en, reverse=True)
    return todos_recursos


@router.get("/{recurso_id}", response_model=RecursoConOrigen)
def ver_recurso(
    recurso_id: int,
    docente: DocenteActualDep,
    db: DBDep
):
    recurso = db.execute(
        select(Recurso).where(Recurso.id == recurso_id)
    ).scalar_one_or_none()

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    es_dueno = recurso.docente_id == docente.id

    if not es_dueno:
        compartido = db.execute(
            select(RecursoCompartido).where(
                RecursoCompartido.recurso_id == recurso_id,
                RecursoCompartido.compartido_con_id == docente.id
            )
        ).scalar_one_or_none()

        if not compartido:
            raise HTTPException(status_code=403, detail="No tienes acceso a este recurso")

    origen = "propio" if es_dueno else "compartido"
    compartido_por = None

    if not es_dueno:
        dueno = db.execute(
            select(Docente).where(Docente.id == recurso.docente_id)
        ).scalar_one()
        compartido_por = dueno.nombre

    favorito = db.execute(
        select(Favorito).where(
            Favorito.docente_id == docente.id,
            Favorito.recurso_id == recurso.id
        )
    ).first()

    return RecursoConOrigen(
        id=recurso.id,
        docente_id=recurso.docente_id,
        tipo=recurso.tipo,
        titulo=recurso.titulo,
        prompt_usuario=recurso.prompt_usuario,
        modo_proyeccion=recurso.modo_proyeccion,
        html_content=recurso.html_content,
        creado_en=recurso.creado_en,
        origen=origen,
        compartido_por=compartido_por,
        es_favorito=favorito is not None
    )


@router.patch("/{recurso_id}/favorito")
def toggle_favorito(
    recurso_id: int,
    docente: DocenteActualDep,
    db: DBDep
):
    recurso = db.execute(
        select(Recurso).where(Recurso.id == recurso_id)
    ).scalar_one_or_none()

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    es_dueno = recurso.docente_id == docente.id

    if not es_dueno:
        compartido = db.execute(
            select(RecursoCompartido).where(
                RecursoCompartido.recurso_id == recurso_id,
                RecursoCompartido.compartido_con_id == docente.id
            )
        ).scalar_one_or_none()

        if not compartido:
            raise HTTPException(status_code=403, detail="No tienes acceso a este recurso")

    favorito_existente = db.execute(
        select(Favorito).where(
            Favorito.docente_id == docente.id,
            Favorito.recurso_id == recurso_id
        )
    ).scalar_one_or_none()

    if favorito_existente:
        db.delete(favorito_existente)
        db.commit()
        return {"mensaje": "Favorito eliminado", "es_favorito": False}
    else:
        nuevo_favorito = Favorito(docente_id=docente.id, recurso_id=recurso_id)
        db.add(nuevo_favorito)
        db.commit()
        return {"mensaje": "Favorito agregado", "es_favorito": True}


@router.delete("/{recurso_id}")
def eliminar_recurso(
    recurso_id: int,
    docente: DocenteActualDep,
    db: DBDep
):
    recurso = db.execute(
        select(Recurso).where(Recurso.id == recurso_id)
    ).scalar_one_or_none()

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    if recurso.docente_id != docente.id:
        raise HTTPException(status_code=403, detail="Solo el dueño original puede eliminar el recurso")

    # Eliminar favoritos
    favoritos = db.execute(
        select(Favorito).where(Favorito.recurso_id == recurso_id)
    ).scalars().all()
    for f in favoritos:
        db.delete(f)

    # Eliminar compartidos
    compartidos = db.execute(
        select(RecursoCompartido).where(RecursoCompartido.recurso_id == recurso_id)
    ).scalars().all()
    for c in compartidos:
        db.delete(c)

    db.delete(recurso)
    db.commit()

    return {"mensaje": "Recurso eliminado correctamente"}

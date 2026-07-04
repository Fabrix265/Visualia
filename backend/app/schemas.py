from datetime import datetime
from pydantic import BaseModel, ConfigDict


# --- Docente ---
class DocenteCreate(BaseModel):
    nombre: str
    password: str


class DocenteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    creado_en: datetime


# --- Sesion ---
class SesionCreate(BaseModel):
    nombre: str
    password: str


class SesionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    token: str


# --- Recurso ---
class RecursoCreate(BaseModel):
    tipo: str  # ficha, hoja_grafica, afiche, lamina
    titulo: str
    prompt_usuario: str
    modo_proyeccion: bool = False


class RecursoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    docente_id: int
    tipo: str
    titulo: str
    prompt_usuario: str
    modo_proyeccion: bool
    html_content: str | None
    creado_en: datetime


# --- Favorito ---
class FavoritoCreate(BaseModel):
    recurso_id: int


class FavoritoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    docente_id: int
    recurso_id: int
    creado_en: datetime


# --- RecursoCompartido ---
class CompartirCreate(BaseModel):
    recurso_id: int
    compartido_con_id: int


class CompartirResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    recurso_id: int
    compartido_por_id: int
    compartido_con_id: int
    creado_en: datetime


# --- EnlacePublico ---
class EnlacePublicoCreate(BaseModel):
    recurso_id: int


class EnlacePublicoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    recurso_id: int
    token: str
    creado_en: datetime


# --- Buscar Docente ---
class DocenteBusqueda(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str

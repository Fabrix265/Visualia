from datetime import datetime
from pydantic import BaseModel


# --- Docente ---
class DocenteCreate(BaseModel):
    nombre: str
    password: str


class DocenteResponse(BaseModel):
    id: int
    nombre: str
    creado_en: datetime

    class Config:
        from_attributes = True


# --- Sesion ---
class SesionCreate(BaseModel):
    nombre: str
    password: str


class SesionResponse(BaseModel):
    token: str

    class Config:
        from_attributes = True


# --- Recurso ---
class RecursoCreate(BaseModel):
    tipo: str  # ficha, hoja_grafica, afiche, lamina
    titulo: str
    prompt_usuario: str
    modo_proyeccion: bool = False


class RecursoResponse(BaseModel):
    id: int
    docente_id: int
    tipo: str
    titulo: str
    prompt_usuario: str
    modo_proyeccion: bool
    html_content: str | None
    creado_en: datetime

    class Config:
        from_attributes = True


# --- Favorito ---
class FavoritoCreate(BaseModel):
    recurso_id: int


class FavoritoResponse(BaseModel):
    id: int
    docente_id: int
    recurso_id: int
    creado_en: datetime

    class Config:
        from_attributes = True


# --- RecursoCompartido ---
class CompartirCreate(BaseModel):
    recurso_id: int
    compartido_con_id: int


class CompartirResponse(BaseModel):
    id: int
    recurso_id: int
    compartido_por_id: int
    compartido_con_id: int
    creado_en: datetime

    class Config:
        from_attributes = True


# --- EnlacePublico ---
class EnlacePublicoCreate(BaseModel):
    recurso_id: int


class EnlacePublicoResponse(BaseModel):
    id: int
    recurso_id: int
    token: str
    creado_en: datetime

    class Config:
        from_attributes = True


# --- Buscar Docente ---
class DocenteBusqueda(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True

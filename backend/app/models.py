from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from app.database import Base


class Docente(Base):
    __tablename__ = "docentes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    sesiones = relationship("Sesion", back_populates="docente")
    recursos = relationship("Recurso", back_populates="docente")
    favoritos = relationship("Favorito", back_populates="docente")


class Sesion(Base):
    __tablename__ = "sesiones"

    id = Column(Integer, primary_key=True, index=True)
    docente_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)
    token = Column(String, unique=True, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    docente = relationship("Docente", back_populates="sesiones")


class Recurso(Base):
    __tablename__ = "recursos"

    id = Column(Integer, primary_key=True, index=True)
    docente_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)
    tipo = Column(String, nullable=False)  # ficha, hoja_grafica, lamina, instructivo, kit_de_imprevistos, medidor_de_grupo, historia_participativa, laboratorio_de_preguntas, clasificador_interactivo, secuencia_logica, encontrar_diferencias
    titulo = Column(String, nullable=False)
    prompt_usuario = Column(Text, nullable=False)
    modo_proyeccion = Column(Boolean, default=False)
    html_content = Column(Text, nullable=True)
    creado_en = Column(DateTime, default=datetime.utcnow)

    docente = relationship("Docente", back_populates="recursos")
    favoritos = relationship("Favorito", back_populates="recurso")
    compartidos = relationship("RecursoCompartido", back_populates="recurso")
    enlaces_publicos = relationship("EnlacePublico", back_populates="recurso")


class Favorito(Base):
    __tablename__ = "favoritos"

    id = Column(Integer, primary_key=True, index=True)
    docente_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)
    recurso_id = Column(Integer, ForeignKey("recursos.id"), nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (UniqueConstraint("docente_id", "recurso_id"),)

    docente = relationship("Docente", back_populates="favoritos")
    recurso = relationship("Recurso", back_populates="favoritos")


class RecursoCompartido(Base):
    __tablename__ = "recursos_compartidos"

    id = Column(Integer, primary_key=True, index=True)
    recurso_id = Column(Integer, ForeignKey("recursos.id"), nullable=False)
    compartido_por_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)
    compartido_con_id = Column(Integer, ForeignKey("docentes.id"), nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (UniqueConstraint("recurso_id", "compartido_con_id"),)

    recurso = relationship("Recurso", back_populates="compartidos")
    compartido_por = relationship("Docente", foreign_keys=[compartido_por_id])
    compartido_con = relationship("Docente", foreign_keys=[compartido_con_id])


class EnlacePublico(Base):
    __tablename__ = "enlaces_publicos"

    id = Column(Integer, primary_key=True, index=True)
    recurso_id = Column(Integer, ForeignKey("recursos.id"), nullable=False)
    token = Column(String, unique=True, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    recurso = relationship("Recurso", back_populates="enlaces_publicos")

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.models import Docente, Sesion, Recurso, Favorito, RecursoCompartido, EnlacePublico

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def docente_creado(client, db_session):
    response = client.post(
        "/auth/registro",
        json={"nombre": "test_profesor", "password": "test123"}
    )
    data = response.json()
    token = data["token"]
    sesion = db_session.query(Sesion).filter(Sesion.token == token).first()
    docente = db_session.query(Docente).filter(Docente.id == sesion.docente_id).first()
    return {"id": docente.id, "nombre": docente.nombre, "token": token}


@pytest.fixture
def token_docente(docente_creado):
    return docente_creado["token"]


@pytest.fixture
def headers_auth(token_docente):
    return {"Authorization": f"Bearer {token_docente}"}

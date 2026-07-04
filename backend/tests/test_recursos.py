from tests.conftest import *
from app.models import Recurso, RecursoCompartido, Favorito, Docente
from app.core.security import hash_password


class TestMisRecursos:
    """Tests para GET /recursos/mis-recursos"""

    def test_mis_recursos_vacio(self, client, headers_auth):
        """Lista vacía cuando no hay recursos"""
        response = client.get("/recursos/mis-recursos", headers=headers_auth)
        assert response.status_code == 200
        assert response.json() == []

    def test_mis_recursos_con_recursos_propios(self, client, db_session, docente_creado, headers_auth):
        """Retorna recursos propios"""
        recurso1 = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Ficha de colores",
            prompt_usuario="Crea una ficha de colores",
            modo_proyeccion=False,
            html_content="<html><body>Ficha 1</body></html>"
        )
        recurso2 = Recurso(
            docente_id=docente_creado["id"],
            tipo="afiche",
            titulo="Afiche de seguridad",
            prompt_usuario="Crea un afiche",
            modo_proyeccion=True,
            html_content="<html><body>Afiche</body></html>"
        )
        db_session.add_all([recurso1, recurso2])
        db_session.commit()

        response = client.get("/recursos/mis-recursos", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert data[0]["origen"] == "propio"
        assert data[0]["compartido_por"] is None

    def test_mis_recursos_con_recursos_compartidos(self, client, db_session, docente_creado, headers_auth):
        """Retorna recursos compartidos por otro docente"""
        otro_docente = Docente(
            nombre="otro_docente",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=otro_docente.id,
            tipo="lamina",
            titulo="Lamina compartida",
            prompt_usuario="Crea una lamina",
            modo_proyeccion=False,
            html_content="<html><body>Lamina</body></html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        compartido = RecursoCompartido(
            recurso_id=recurso.id,
            compartido_por_id=otro_docente.id,
            compartido_con_id=docente_creado["id"]
        )
        db_session.add(compartido)
        db_session.commit()

        response = client.get("/recursos/mis-recursos", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["origen"] == "compartido"
        assert data[0]["compartido_por"] == "otro_docente"

    def test_mis_recursos_filtro_tipo(self, client, db_session, docente_creado, headers_auth):
        """Filtra por tipo"""
        recurso1 = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Ficha",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        recurso2 = Recurso(
            docente_id=docente_creado["id"],
            tipo="afiche",
            titulo="Afiche",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add_all([recurso1, recurso2])
        db_session.commit()

        response = client.get("/recursos/mis-recursos?tipo=ficha", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["tipo"] == "ficha"

    def test_mis_recursos_sin_token(self, client):
        """Requiere autenticación"""
        response = client.get("/recursos/mis-recursos")
        assert response.status_code == 401


class TestVerRecurso:
    """Tests para GET /recursos/{id}"""

    def test_ver_recurso_propio(self, client, db_session, docente_creado, headers_auth):
        """Puede ver su propio recurso"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Mi ficha",
            prompt_usuario="test",
            html_content="<html><body>Mi ficha</body></html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.get(f"/recursos/{recurso.id}", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert data["titulo"] == "Mi ficha"
        assert data["origen"] == "propio"

    def test_ver_recurso_compartido(self, client, db_session, docente_creado, headers_auth):
        """Puede ver recurso compartido"""
        otro_docente = Docente(
            nombre="otro_docente",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=otro_docente.id,
            tipo="lamina",
            titulo="Lamina compartida",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        compartido = RecursoCompartido(
            recurso_id=recurso.id,
            compartido_por_id=otro_docente.id,
            compartido_con_id=docente_creado["id"]
        )
        db_session.add(compartido)
        db_session.commit()

        response = client.get(f"/recursos/{recurso.id}", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert data["origen"] == "compartido"
        assert data["compartido_por"] == "otro_docente"

    def test_ver_recurso_sin_acceso(self, client, db_session, headers_auth):
        """No puede ver recurso de otro sin compartir"""
        otro_docente = Docente(
            nombre="otro_docente",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=otro_docente.id,
            tipo="ficha",
            titulo="Privada",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.get(f"/recursos/{recurso.id}", headers=headers_auth)
        assert response.status_code == 403

    def test_ver_recurso_no_existe(self, client, headers_auth):
        """Recurso no encontrado"""
        response = client.get("/recursos/999", headers=headers_auth)
        assert response.status_code == 404


class TestToggleFavorito:
    """Tests para PATCH /recursos/{id}/favorito"""

    def test_agregar_favorito(self, client, db_session, docente_creado, headers_auth):
        """Agrega recurso a favoritos"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Ficha favorita",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.patch(f"/recursos/{recurso.id}/favorito", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert data["es_favorito"] is True

        favorito = db_session.query(Favorito).filter(
            Favorito.docente_id == docente_creado["id"],
            Favorito.recurso_id == recurso.id
        ).first()
        assert favorito is not None

    def test_eliminar_favorito(self, client, db_session, docente_creado, headers_auth):
        """Elimina recurso de favoritos"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Ficha favorita",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        favorito = Favorito(
            docente_id=docente_creado["id"],
            recurso_id=recurso.id
        )
        db_session.add(favorito)
        db_session.commit()

        response = client.patch(f"/recursos/{recurso.id}/favorito", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert data["es_favorito"] is False

    def test_toggle_favorito_compartido(self, client, db_session, docente_creado, headers_auth):
        """Puede marcar como favorito un recurso compartido"""
        otro_docente = Docente(
            nombre="otro_docente",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=otro_docente.id,
            tipo="lamina",
            titulo="Lamina para favorito",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        compartido = RecursoCompartido(
            recurso_id=recurso.id,
            compartido_por_id=otro_docente.id,
            compartido_con_id=docente_creado["id"]
        )
        db_session.add(compartido)
        db_session.commit()

        response = client.patch(f"/recursos/{recurso.id}/favorito", headers=headers_auth)
        assert response.status_code == 200
        assert response.json()["es_favorito"] is True

    def test_favorito_sin_acceso(self, client, db_session, headers_auth):
        """No puede marcar favorito sin acceso"""
        otro_docente = Docente(
            nombre="otro_docente",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=otro_docente.id,
            tipo="ficha",
            titulo="Privada",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.patch(f"/recursos/{recurso.id}/favorito", headers=headers_auth)
        assert response.status_code == 403


class TestEliminarRecurso:
    """Tests para DELETE /recursos/{id}"""

    def test_eliminar_recurso_propio(self, client, db_session, docente_creado, headers_auth):
        """Puede eliminar su propio recurso"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Para eliminar",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.delete(f"/recursos/{recurso.id}", headers=headers_auth)
        assert response.status_code == 200

        recurso_db = db_session.query(Recurso).filter(Recurso.id == recurso.id).first()
        assert recurso_db is None

    def test_eliminar_recurso_con_favoritos_y_compartidos(self, client, db_session, docente_creado, headers_auth):
        """Elimina recurso con favoritos y compartidos"""
        otro_docente = Docente(
            nombre="otro_docente",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="afiche",
            titulo="Con relaciones",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        favorito = Favorito(
            docente_id=docente_creado["id"],
            recurso_id=recurso.id
        )
        db_session.add(favorito)

        compartido = RecursoCompartido(
            recurso_id=recurso.id,
            compartido_por_id=docente_creado["id"],
            compartido_con_id=otro_docente.id
        )
        db_session.add(compartido)
        db_session.commit()

        response = client.delete(f"/recursos/{recurso.id}", headers=headers_auth)
        assert response.status_code == 200

        assert db_session.query(Recurso).filter(Recurso.id == recurso.id).first() is None
        assert db_session.query(Favorito).filter(Favorito.recurso_id == recurso.id).first() is None
        assert db_session.query(RecursoCompartido).filter(RecursoCompartido.recurso_id == recurso.id).first() is None

    def test_eliminar_recurso_ajeno(self, client, db_session, headers_auth):
        """No puede eliminar recurso de otro"""
        otro_docente = Docente(
            nombre="otro_docente",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=otro_docente.id,
            tipo="ficha",
            titulo="Ajena",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.delete(f"/recursos/{recurso.id}", headers=headers_auth)
        assert response.status_code == 403

    def test_eliminar_recurso_no_existe(self, client, headers_auth):
        """Recurso no encontrado"""
        response = client.delete("/recursos/999", headers=headers_auth)
        assert response.status_code == 404

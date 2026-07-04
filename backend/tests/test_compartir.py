from tests.conftest import *
from app.models import Recurso, RecursoCompartido, EnlacePublico, Docente
from app.core.security import hash_password


class TestCompartirConDocente:
    """Tests para POST /recursos/{id}/compartir-con-docente"""

    def test_compartir_exitoso(self, client, db_session, docente_creado, headers_auth):
        """Comparte un recurso con otro docente"""
        otro_docente = Docente(
            nombre="destino",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Para compartir",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.post(
            f"/recursos/{recurso.id}/compartir-con-docente?docente_destino_id={otro_docente.id}",
            headers=headers_auth
        )
        assert response.status_code == 200
        data = response.json()
        assert data["recurso_id"] == recurso.id
        assert data["compartido_por_id"] == docente_creado["id"]
        assert data["compartido_con_id"] == otro_docente.id

    def test_compartir_mismo_recurso_dos_veces(self, client, db_session, docente_creado, headers_auth):
        """No duplica si se comparte dos veces"""
        otro_docente = Docente(
            nombre="destino",
            password_hash=hash_password("pass123")
        )
        db_session.add(otro_docente)
        db_session.commit()
        db_session.refresh(otro_docente)

        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Doble compartición",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        client.post(
            f"/recursos/{recurso.id}/compartir-con-docente?docente_destino_id={otro_docente.id}",
            headers=headers_auth
        )

        response = client.post(
            f"/recursos/{recurso.id}/compartir-con-docente?docente_destino_id={otro_docente.id}",
            headers=headers_auth
        )
        assert response.status_code == 200

        compartidos = db_session.query(RecursoCompartido).filter(
            RecursoCompartido.recurso_id == recurso.id
        ).count()
        assert compartidos == 1

    def test_compartir_recurso_ajeno(self, client, db_session, headers_auth):
        """No puede compartir recurso de otro"""
        otro_docente = Docente(
            nombre="dueno",
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

        response = client.post(
            f"/recursos/{recurso.id}/compartir-con-docente?docente_destino_id={otro_docente.id}",
            headers=headers_auth
        )
        assert response.status_code == 403

    def test_compartir_con_si_mismo(self, client, db_session, docente_creado, headers_auth):
        """No puede compartir consigo mismo"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Auto-compartir",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.post(
            f"/recursos/{recurso.id}/compartir-con-docente?docente_destino_id={docente_creado['id']}",
            headers=headers_auth
        )
        assert response.status_code == 400

    def test_compartir_recurso_no_existe(self, client, headers_auth):
        """Recurso no encontrado"""
        response = client.post(
            "/recursos/999/compartir-con-docente?docente_destino_id=1",
            headers=headers_auth
        )
        assert response.status_code == 404


class TestEnlacePublico:
    """Tests para POST /recursos/{id}/enlace-publico"""

    def test_crear_enlace(self, client, db_session, docente_creado, headers_auth):
        """Crea enlace público"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="afiche",
            titulo="Para TV",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response = client.post(f"/recursos/{recurso.id}/enlace-publico", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert data["recurso_id"] == recurso.id
        assert data["token"] is not None

    def test_reutilizar_enlace(self, client, db_session, docente_creado, headers_auth):
        """Reutiliza enlace existente"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="afiche",
            titulo="Reutilizar",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        response1 = client.post(f"/recursos/{recurso.id}/enlace-publico", headers=headers_auth)
        token1 = response1.json()["token"]

        response2 = client.post(f"/recursos/{recurso.id}/enlace-publico", headers=headers_auth)
        token2 = response2.json()["token"]

        assert token1 == token2

    def test_enlace_recurso_ajeno(self, client, db_session, headers_auth):
        """No puede crear enlace de recurso ajeno"""
        otro_docente = Docente(
            nombre="dueno",
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

        response = client.post(f"/recursos/{recurso.id}/enlace-publico", headers=headers_auth)
        assert response.status_code == 403


class TestVerRecursoPublico:
    """Tests para GET /compartido/{token}"""

    def test_ver_recurso_publico(self, client, db_session, docente_creado, headers_auth):
        """Puede ver recurso público sin autenticación"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="lamina",
            titulo="Publica",
            prompt_usuario="test",
            html_content="<html><body>Publico</body></html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        enlace = EnlacePublico(
            recurso_id=recurso.id,
            token="token-test-123"
        )
        db_session.add(enlace)
        db_session.commit()

        response = client.get("/compartido/token-test-123")
        assert response.status_code == 200
        data = response.json()
        assert data["titulo"] == "Publica"
        assert data["html_content"] == "<html><body>Publico</body></html>"

    def test_token_no_existe(self, client):
        """Token no válido"""
        response = client.get("/compartido/token-inexistente")
        assert response.status_code == 404

    def test_recurso_eliminado(self, client, db_session, docente_creado, headers_auth):
        """Recurso eliminado pero enlace existe"""
        recurso = Recurso(
            docente_id=docente_creado["id"],
            tipo="ficha",
            titulo="Eliminada",
            prompt_usuario="test",
            html_content="<html>test</html>"
        )
        db_session.add(recurso)
        db_session.commit()
        db_session.refresh(recurso)

        enlace = EnlacePublico(
            recurso_id=recurso.id,
            token="token-eliminado"
        )
        db_session.add(enlace)
        db_session.commit()

        # Eliminar el enlace primero, luego el recurso
        db_session.delete(enlace)
        db_session.commit()

        db_session.delete(recurso)
        db_session.commit()

        response = client.get("/compartido/token-eliminado")
        assert response.status_code == 404

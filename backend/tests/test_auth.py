import pytest


class TestRegistro:
    def test_registro_exitoso(self, client):
        response = client.post(
            "/auth/registro",
            json={"nombre": "nuevo_profesor", "password": "pass123"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert len(data["token"]) > 0

    def test_registro_nombre_duplicado(self, client, docente_creado):
        response = client.post(
            "/auth/registro",
            json={"nombre": "test_profesor", "password": "otro_pass"}
        )
        assert response.status_code == 400
        assert "ya esta en uso" in response.json()["detail"]

    def test_registro_campos_requeridos(self, client):
        response = client.post("/auth/registro", json={})
        assert response.status_code == 422


class TestLogin:
    def test_login_exitoso(self, client, docente_creado):
        response = client.post(
            "/auth/login",
            json={"nombre": "test_profesor", "password": "test123"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert len(data["token"]) > 0

    def test_login_password_incorrecto(self, client, docente_creado):
        response = client.post(
            "/auth/login",
            json={"nombre": "test_profesor", "password": "wrong_pass"}
        )
        assert response.status_code == 401
        assert "incorrectos" in response.json()["detail"]

    def test_login_usuario_inexistente(self, client):
        response = client.post(
            "/auth/login",
            json={"nombre": "no_existe", "password": "pass"}
        )
        assert response.status_code == 401


class TestLogout:
    def test_logout_exitoso(self, client, headers_auth):
        response = client.post("/auth/logout", headers=headers_auth)
        assert response.status_code == 200
        assert "cerrada" in response.json()["mensaje"]

    def test_logout_sin_token(self, client):
        response = client.post("/auth/logout")
        assert response.status_code == 401

    def test_logout_token_invalido(self, client):
        response = client.post(
            "/auth/logout",
            headers={"Authorization": "Bearer token_invalido"}
        )
        assert response.status_code == 401


class TestBuscarDocentes:
    def test_buscar_con_token(self, client, headers_auth, docente_creado):
        response = client.get("/docentes/buscar?q=test", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_buscar_sin_token(self, client):
        response = client.get("/docentes/buscar?q=test")
        assert response.status_code == 401

    def test_buscar_excluye_usuario_actual(self, client, headers_auth, docente_creado):
        response = client.get("/docentes/buscar?q=test_profesor", headers=headers_auth)
        assert response.status_code == 200
        data = response.json()
        nombres = [d["nombre"] for d in data]
        assert "test_profesor" not in nombres

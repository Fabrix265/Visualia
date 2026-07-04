# Visualia

Generador de recursos visuales para docentes de nivel inicial. Aplicación web que permite crear fichas, hojas gráficas, afiches y láminas utilizando inteligencia artificial, guardarlos en una biblioteca personal, compartirlos con otros docentes y proyectarlos en pantalla.

## Tech Stack

- **Backend:** FastAPI (Python) + SQLAlchemy + Supabase Postgres
- **Frontend:** React + Vite + Tailwind CSS
- **IA:** Gemini API (Google)

## Cómo correr en local

### Backend

```bash
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Copiar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de Supabase y API keys de Gemini

# Levantar servidor
uvicorn app.main:app --reload
```

El backend estará disponible en `http://localhost:8000`. La documentación Swagger se puede acceder en `http://localhost:8000/docs`.

### Frontend

```bash
cd frontend

# Instalar dependencias
npm install

# Copiar variables de entorno
cp .env.example .env
# Editar .env con la URL del backend

# Levantar servidor de desarrollo
npm run dev
```

El frontend estará disponible en `http://localhost:5173`.

## Estructura del proyecto

```
Visualia/
├── backend/          # API REST con FastAPI
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── routers/
│   │   ├── services/
│   │   └── templates_ia/
│   └── requirements.txt
├── frontend/         # Aplicación React con Vite
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   └── styles/
│   └── package.json
└── README.md
```

import re
import requests
import time
from app.config import GEMINI_API_KEYS

MODELO = "gemini-2.5-flash"
MAX_REINTENTOS = 3
PAUSA_ENTRE_REINTENTOS = 2


def _limpiar_respuesta_ia(texto: str) -> str:
    """
    Gemini casi siempre envuelve el HTML en bloques de código markdown
    (```html ... ``` o ``` ... ```) aunque se le pida no hacerlo.
    Esta función quita esos fences y cualquier texto suelto antes/después
    del documento HTML real, para que lo que se guarda en la BD sea
    HTML puro y no se vea como texto roto al renderizarlo.
    """
    if not texto:
        return texto

    limpio = texto.strip()

    # Quita fences de markdown tipo ```html ... ``` o ``` ... ```
    fence_match = re.match(r"^```[a-zA-Z]*\s*\n?(.*?)\n?```\s*$", limpio, re.DOTALL)
    if fence_match:
        limpio = fence_match.group(1).strip()
    else:
        # Por si el modelo dejó solo el fence de apertura o de cierre suelto
        limpio = re.sub(r"^```[a-zA-Z]*\s*\n?", "", limpio)
        limpio = re.sub(r"\n?```\s*$", "", limpio)

    # Si aún así hay texto antes de <!DOCTYPE o <html>, recorta hasta ahí
    inicio_html = re.search(r"(<!DOCTYPE html|<html)", limpio, re.IGNORECASE)
    if inicio_html and inicio_html.start() > 0:
        limpio = limpio[inicio_html.start():]

    return limpio.strip()


class GeminiClient:
    def __init__(self):
        self.keys = GEMINI_API_KEYS
        self.current_index = 0

    def _get_next_key(self) -> str:
        key = self.keys[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.keys)
        return key

    def generate_content(self, prompt: str) -> str:
        if not self.keys:
            raise ValueError("No hay API keys de Gemini configuradas en .env")

        for _ in range(len(self.keys)):
            api_key = self._get_next_key()
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELO}:generateContent?key={api_key}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }

            for intento in range(1, MAX_REINTENTOS + 1):
                try:
                    response = requests.post(
                        url,
                        headers={"Content-Type": "application/json"},
                        json=payload,
                        timeout=60
                    )

                    if response.status_code == 429:
                        time.sleep(PAUSA_ENTRE_REINTENTOS)
                        continue

                    if response.status_code != 200:
                        if intento < MAX_REINTENTOS:
                            time.sleep(PAUSA_ENTRE_REINTENTOS)
                        continue

                    data = response.json()
                    texto_bruto = data["candidates"][0]["content"]["parts"][0]["text"]
                    return _limpiar_respuesta_ia(texto_bruto)

                except Exception:
                    if intento < MAX_REINTENTOS:
                        time.sleep(PAUSA_ENTRE_REINTENTOS)
                    continue

        raise ValueError(
            "Todas las API keys fallaron. Intentá de nuevo."
        )


gemini_client = GeminiClient()

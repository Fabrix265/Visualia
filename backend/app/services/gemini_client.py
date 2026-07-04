import requests
import time
from app.config import GEMINI_API_KEYS

MODELO = "gemini-2.5-flash"
MAX_REINTENTOS = 3
PAUSA_ENTRE_REINTENTOS = 2


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
                    return data["candidates"][0]["content"]["parts"][0]["text"]

                except Exception:
                    if intento < MAX_REINTENTOS:
                        time.sleep(PAUSA_ENTRE_REINTENTOS)
                    continue

        raise ValueError(
            "Todas las API keys fallaron. Intentá de nuevo."
        )


gemini_client = GeminiClient()

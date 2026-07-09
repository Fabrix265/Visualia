import base64
import random
import time
import requests
from urllib.parse import quote

BASE_URL = "https://image.pollinations.ai/prompt"
MAX_REINTENTOS = 3
PAUSA_ENTRE_REINTENTOS = 3


class PollinationsClient:
    def generar_imagen(self, prompt: str) -> dict:
        prompt_codificado = quote(prompt)
        url = (
            f"{BASE_URL}/{prompt_codificado}"
            f"?width=768&height=1024"
            f"&model=flux&nologo=true"
            f"&seed={random.randint(1, 999999)}"
        )

        for intento in range(1, MAX_REINTENTOS + 1):
            try:
                response = requests.get(url, timeout=120)

                if response.status_code == 429:
                    time.sleep(PAUSA_ENTRE_REINTENTOS)
                    continue

                if response.status_code != 200:
                    if intento < MAX_REINTENTOS:
                        time.sleep(PAUSA_ENTRE_REINTENTOS)
                    continue

                content_type = response.headers.get("Content-Type", "image/png")
                if "image" not in content_type:
                    if intento < MAX_REINTENTOS:
                        time.sleep(PAUSA_ENTRE_REINTENTOS)
                    continue

                image_base64 = base64.b64encode(response.content).decode("utf-8")

                return {
                    "image_base64": image_base64,
                    "mime_type": content_type.split(";")[0].strip(),
                }

            except Exception:
                if intento < MAX_REINTENTOS:
                    time.sleep(PAUSA_ENTRE_REINTENTOS)
                continue

        raise ValueError(
            "No se pudo generar la imagen. Intentá de nuevo en unos segundos."
        )


pollinations_client = PollinationsClient()

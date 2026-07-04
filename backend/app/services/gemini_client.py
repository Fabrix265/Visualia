import google.generativeai as genai
from app.config import GEMINI_API_KEYS


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

        last_error = None
        for i in range(len(self.keys)):
            api_key = self._get_next_key()
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                last_error = e
                error_msg = str(e).lower()
                if "429" in error_msg or "quota" in error_msg or "rate" in error_msg:
                    continue
                if "api_key" in error_msg or "invalid" in error_msg or "permission" in error_msg:
                    raise ValueError(
                        f"API key inválida o sin permisos. "
                        f"Verifica que las GEMINI_API_KEYS en .env sean válidas. "
                        f"Error: {str(e)[:100]}"
                    )
                continue

        raise ValueError(
            "Todas las API keys de Gemini agotadas o con errores. "
            "Intenta de nuevo en un momento."
        )


gemini_client = GeminiClient()

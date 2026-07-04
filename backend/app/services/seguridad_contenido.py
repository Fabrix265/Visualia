import re
from fastapi import HTTPException

PALABRAS_PROHIBIDAS = [
    "violencia", "arma", "droga", "alcohol", "tabaco",
    "muerte", "matar", "odio", "racismo", "discriminación",
]

LONGITUD_MINIMA = 100


def validar_html(html_content: str) -> str:
    if not html_content or len(html_content.strip()) < LONGITUD_MINIMA:
        raise HTTPException(
            status_code=400,
            detail="El contenido generado es demasiado corto. Intenta con una descripción más detallada."
        )

    html_lower = html_content.lower()
    for palabra in PALABRAS_PROHIBIDAS:
        if palabra in html_lower:
            raise HTTPException(
                status_code=400,
                detail="El contenido generado no es apropiado. Intenta con otra solicitud."
            )

    if not re.search(r"<html[^>]*>", html_lower) or not re.search(r"</html>", html_lower):
        raise HTTPException(
            status_code=400,
            detail="El contenido generado no es un HTML válido. Intenta de nuevo."
        )

    return html_content

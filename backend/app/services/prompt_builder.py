from app.templates_ia.base_estilos import BASE_ESTILOS
from app.templates_ia.ficha import FICHA_INSTRUCCIONES
from app.templates_ia.hoja_grafica import HOJA_GRAFICA_INSTRUCCIONES
from app.templates_ia.afiche import AFICHE_INSTRUCCIONES
from app.templates_ia.lamina import LAMINA_INSTRUCCIONES

INSTRUCCIONES_TIPO = {
    "ficha": FICHA_INSTRUCCIONES,
    "hoja_grafica": HOJA_GRAFICA_INSTRUCCIONES,
    "afiche": AFICHE_INSTRUCCIONES,
    "lamina": LAMINA_INSTRUCCIONES,
}

MODO_PROYECCION = """
INSTRUCCIONES ADICIONALES PARA MODO PROYECCIÓN:
- Tipografía MUY grande (mínimo 24px para texto, 48px para títulos)
- Diseño centrado y a pantalla completa
- Alto contraste para verse bien proyectado
- Sin elementos pensados para imprimir
- Sin bordes de página o márgenes de impresión
- Fondos sólidos o degradados suaves
"""

INSTRUCCION_FINAL = """
Responde ÚNICAMENTE con un documento HTML completo y autocontenido
(incluye CSS y JS dentro del mismo HTML). No agregues explicaciones
fuera del HTML. El HTML debe funcionar independientemente.
"""


def construir_prompt(tipo: str, prompt_usuario: str, modo_proyeccion: bool = False) -> str:
    if tipo not in INSTRUCCIONES_TIPO:
        raise ValueError(f"Tipo de recurso no válido: {tipo}. Tipos válidos: {list(INSTRUCCIONES_TIPO.keys())}")

    partes = [
        "Eres un asistente especializado en crear recursos visuales para docentes de nivel inicial.",
        "",
        BASE_ESTILOS,
        "",
        INSTRUCCIONES_TIPO[tipo],
    ]

    if modo_proyeccion:
        partes.append(MODO_PROYECCION)

    partes.extend([
        "",
        "SOLICITUD DEL USUARIO:",
        prompt_usuario,
        "",
        INSTRUCCION_FINAL,
    ])

    return "\n".join(partes)

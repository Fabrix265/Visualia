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

NOMBRES_TIPO = {
    "ficha": "una FICHA (hoja de trabajo individual para imprimir)",
    "hoja_grafica": "una HOJA GRÁFICA (actividad visual con poco o nada de texto)",
    "afiche": "un AFICHE (para pegar en la pared, se lee de lejos)",
    "lamina": "una LÁMINA (apoyo informativo para mostrar al grupo)",
}

ROL_SISTEMA = """
Sos el motor de generación de recursos de Visualia, una app que ayuda a docentes
de nivel inicial (niños de 3 a 5 años) a crear material didáctico en segundos.

Tu única salida es un archivo HTML autocontenido, listo para imprimir en A4 y
también presentable en pantalla. No sos un asistente de chat: no conversás,
no hacés preguntas de vuelta, no explicás lo que hiciste. Directamente producís
el documento final, completo y correcto, en un solo intento.
"""

MODO_PROYECCION = """
INSTRUCCIONES ADICIONALES PARA MODO PROYECCIÓN:
Este recurso se va a mostrar en una pantalla o proyector frente al grupo, NO se
va a imprimir. Ajustá el diseño para eso:
- Tipografía muy grande (mínimo 24px texto, 48px+ títulos)
- Diseño centrado y pensado para pantalla completa (usar todo el viewport)
- Alto contraste, para que se vea bien incluso con luz ambiente
- Eliminar por completo cualquier elemento pensado para impresión (bordes de
  hoja, márgenes tipo A4, líneas para escribir a mano)
- Fondos sólidos o degradados suaves dentro de la paleta pastel permitida
- El @media print de la base de estilos puede omitirse en este modo
"""

CHECKLIST_FINAL = """
ANTES DE RESPONDER, verificá en silencio (sin mostrar este análisis):
1. ¿Usé únicamente los colores de la paleta pastel indicada, y ningún otro?
2. ¿El texto principal está en el tono oscuro indicado, no en negro puro?
3. ¿Cargué Fredoka + Nunito/Quicksand vía Google Fonts con <link>?
4. ¿Todo el contenido (textos, actividad) es real y específico al pedido del
   docente, sin placeholders ni texto de relleno?
5. ¿El diseño respeta la estructura y características específicas del tipo
   de recurso solicitado?
6. ¿Incluí las reglas de impresión (@page, @media print) salvo que sea modo
   proyección?
7. ¿El HTML es un documento completo y válido, sin texto ni marcas de
   markdown (```), antes o después de las etiquetas <html>...</html>?
Si alguna respuesta es "no", corregilo antes de responder. Después, devolvé
SOLO el HTML final.
"""

INSTRUCCION_FINAL = """
Respondé ÚNICAMENTE con el documento HTML completo y autocontenido (incluye
CSS y JS, si hace falta, dentro del mismo archivo). No agregues explicaciones,
comentarios, ni texto fuera del HTML. No envuelvas la respuesta en bloques de
código markdown (nada de ``` al principio o al final). El HTML debe poder
abrirse y funcionar de forma independiente, sin conexión a internet salvo
para cargar las fuentes de Google Fonts.
"""


def construir_prompt(tipo: str, prompt_usuario: str, modo_proyeccion: bool = False) -> str:
    if tipo not in INSTRUCCIONES_TIPO:
        raise ValueError(f"Tipo de recurso no válido: {tipo}. Tipos válidos: {list(INSTRUCCIONES_TIPO.keys())}")

    partes = [
        ROL_SISTEMA,
        f"Hoy tenés que generar {NOMBRES_TIPO[tipo]}.",
        "",
        BASE_ESTILOS,
        "",
        INSTRUCCIONES_TIPO[tipo],
    ]

    if modo_proyeccion:
        partes.append(MODO_PROYECCION)

    partes.extend([
        "",
        "SOLICITUD DEL DOCENTE (esto define el tema y el contenido real del recurso):",
        f'"""{prompt_usuario}"""',
        "",
        CHECKLIST_FINAL,
        INSTRUCCION_FINAL,
    ])

    return "\n".join(partes)

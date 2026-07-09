from app.templates_ia.base_estilos import BASE_ESTILOS

# --- Antes de la clase (preparación) ---
from app.templates_ia.ficha import FICHA_INSTRUCCIONES
from app.templates_ia.hoja_grafica import HOJA_GRAFICA_INSTRUCCIONES
from app.templates_ia.lamina import LAMINA_INSTRUCCIONES
from app.templates_ia.instructivo import INSTRUCTIVO_INSTRUCCIONES

# --- Durante la clase (en vivo) ---
from app.templates_ia.kit_de_imprevistos import KIT_DE_IMPREVISTOS_INSTRUCCIONES
from app.templates_ia.medidor_de_grupo import MEDIDOR_DE_GRUPO_INSTRUCCIONES
from app.templates_ia.historia_participativa import HISTORIA_PARTICIPATIVA_INSTRUCCIONES

# --- Juegos interactivos de aprendizaje ---
from app.templates_ia.laboratorio_de_preguntas import LABORATORIO_DE_PREGUNTAS_INSTRUCCIONES
from app.templates_ia.clasificador_interactivo import CLASIFICADOR_INTERACTIVO_INSTRUCCIONES
from app.templates_ia.secuencia_logica import SECUENCIA_LOGICA_INSTRUCCIONES
from app.templates_ia.encontrar_diferencias import ENCONTRAR_DIFERENCIAS_INSTRUCCIONES

# NOTA: "afiche" y "pictograma" quedaron fuera del MVP (ver conversación de
# alcance), pero sus archivos siguen en templates_ia/ por si se reincorporan
# más adelante. Alcanza con agregarlos de nuevo a estos dos diccionarios.

INSTRUCCIONES_TIPO = {
    "ficha": FICHA_INSTRUCCIONES,
    "hoja_grafica": HOJA_GRAFICA_INSTRUCCIONES,
    "lamina": LAMINA_INSTRUCCIONES,
    "instructivo": INSTRUCTIVO_INSTRUCCIONES,
    "kit_de_imprevistos": KIT_DE_IMPREVISTOS_INSTRUCCIONES,
    "medidor_de_grupo": MEDIDOR_DE_GRUPO_INSTRUCCIONES,
    "historia_participativa": HISTORIA_PARTICIPATIVA_INSTRUCCIONES,
    "laboratorio_de_preguntas": LABORATORIO_DE_PREGUNTAS_INSTRUCCIONES,
    "clasificador_interactivo": CLASIFICADOR_INTERACTIVO_INSTRUCCIONES,
    "secuencia_logica": SECUENCIA_LOGICA_INSTRUCCIONES,
    "encontrar_diferencias": ENCONTRAR_DIFERENCIAS_INSTRUCCIONES,
}

NOMBRES_TIPO = {
    "ficha": "una FICHA (hoja de trabajo individual para imprimir)",
    "hoja_grafica": "una HOJA GRÁFICA (actividad visual con poco o nada de texto)",
    "lamina": "una LÁMINA (apoyo informativo para mostrar al grupo)",
    "instructivo": "un INSTRUCTIVO (guía paso a paso con materiales y procedimiento)",
    "kit_de_imprevistos": "un KIT DE IMPREVISTOS (varias mini-actividades interactivas para usar en el momento)",
    "medidor_de_grupo": "un MEDIDOR DE GRUPO (actividad interactiva que se adapta al ritmo del grupo con un toque)",
    "historia_participativa": "una HISTORIA PARTICIPATIVA (cuento interactivo con decisiones del grupo)",
    "laboratorio_de_preguntas": "un LABORATORIO DE PREGUNTAS (mini-trivia con feedback inmediato y puntaje)",
    "clasificador_interactivo": "un CLASIFICADOR INTERACTIVO (juego de agrupar elementos por categoría)",
    "secuencia_logica": "una SECUENCIA LÓGICA (juego de ordenar pasos de un proceso)",
    "encontrar_diferencias": "un ENCONTRÁ LAS DIFERENCIAS (juego de atención visual entre dos escenas)",
}

# Tipos cuyo HTML necesita JS con estado (mostrar/ocultar pantallas, contar
# aciertos, etc.) — reciben las reglas técnicas extra de REGLAS_JS_INTERACTIVO
TIPOS_INTERACTIVOS = {
    "kit_de_imprevistos",
    "medidor_de_grupo",
    "historia_participativa",
    "laboratorio_de_preguntas",
    "clasificador_interactivo",
    "secuencia_logica",
    "encontrar_diferencias",
}

REGLAS_JS_INTERACTIVO = """
REGLAS TÉCNICAS OBLIGATORIAS PARA RECURSOS INTERACTIVOS:
Este recurso se ejecuta dentro de un <iframe sandbox="allow-scripts"> (sin
allow-same-origin ni allow-forms), así que el JavaScript tiene restricciones
reales que hay que respetar o el recurso no va a funcionar:
- NUNCA usar localStorage, sessionStorage, cookies ni nada que dependa de
  "origin" — no están disponibles en este sandbox y tirarán error
- NUNCA usar <form> con submit real, ni window.open, ni querer navegar a
  otra URL — todo el estado se maneja mostrando/ocultando <div> con JS puro
- NUNCA usar drag-and-drop nativo del navegador (dragstart/dragover/drop) —
  es poco confiable en pantallas táctiles dentro de un iframe; para
  "mover" o "elegir" algo, usar el patrón tocar-elemento → tocar-destino
- Todo el JS va inline dentro de <script> en el mismo archivo, sin imports,
  sin CDNs, sin dependencias externas de ningún tipo
- Usar solo JavaScript vanilla (document.getElementById, classList,
  addEventListener) — nada de frameworks
- El estado de la interacción se guarda en variables JS normales (se pierde
  si se recarga la página, y está bien que sea así: no hace falta persistirlo)
- El feedback ante una acción del niño (correcto/incorrecto) debe ser
  inmediato y nunca punitivo ni frustrante: siempre se puede reintentar
  sin penalización
- Probar mentalmente el flujo completo de clics antes de responder: cada
  botón debe llevar a un estado válido, nunca a una pantalla en blanco o rota
"""

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

    if tipo in TIPOS_INTERACTIVOS:
        partes.append(REGLAS_JS_INTERACTIVO)

    partes.extend([
        "",
        "SOLICITUD DEL DOCENTE (esto define el tema y el contenido real del recurso):",
        f'"""{prompt_usuario}"""',
        "",
        CHECKLIST_FINAL,
        INSTRUCCION_FINAL,
    ])

    return "\n".join(partes)

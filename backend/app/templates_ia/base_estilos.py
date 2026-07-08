BASE_ESTILOS = """
REGLAS DE ESTILO OBLIGATORIAS (aplicar SIEMPRE, sin excepción):

IDENTIDAD VISUAL "VISUALIA":
Estás generando material para docentes de nivel inicial (niños de 3 a 5 años).
El resultado debe verse como parte de un mismo sistema de diseño: cálido, redondeado,
pastel, nunca infantil-genérico ni recargado.

COLORES (usar SIEMPRE estos valores exactos, nunca inventar otros tonos):
- Fondo general: crema (#FFFDF7)
- Texto principal: gris oscuro suave (#3A3A3A) — nunca negro puro (#000000)
- Paleta pastel (rotar/combinar según la pieza, máximo 2-3 colores por diseño):
  - Azul pastel (#AEE2FF)
  - Rosa pastel (#FFD1E3)
  - Verde menta (#B8F2D0)
  - Lila pastel (#E2D6F3)
  - Durazno pastel (#FFDAB9)
  - Amarillo pastel (#FFF3B0)
- Usar los pasteles como fondos de bloques/tarjetas/acentos, NUNCA como color de texto
  (el texto siempre en #3A3A3A o blanco sobre un fondo oscuro puntual)
- No usar colores fuera de esta paleta, ni degradados saturados, ni negro/gris frío

TIPOGRAFÍA:
- Encabezados y títulos: 'Fredoka' (redondeada, amigable)
- Cuerpo de texto: 'Nunito' o 'Quicksand'
- Cargar SIEMPRE con <link> a Google Fonts (no usar @import, evitar timeouts)
- Incluir fallback: font-family: 'Fredoka', sans-serif; (y similar para el resto)
- Tamaños mínimos: 16px cuerpo, 24px subtítulos, 32px+ títulos (más grande aún
  si el recurso es para niños que aún no leen con fluidez)

ESTILO VISUAL:
- Bordes redondeados en todo (border-radius: 16-24px), sin esquinas rectas duras
- Íconos/SVG grandes, simples y amigables (mínimo 32-40px en elementos interactivos)
- Mucho espacio en blanco: layouts poco saturados, con "aire" entre bloques
- Jerarquía visual clara: un solo elemento protagonista por pantalla/hoja
- Sombras muy sutiles (box-shadow suave tipo 0 2px 8px rgba(0,0,0,0.08)), sin bordes duros
- Ilustraciones solo en SVG inline o emojis grandes; NUNCA referenciar imágenes
  externas (<img src="http://...">) porque no habrá conexión para cargarlas
- Prohibido: imágenes realistas, violentas, tenebrosas o con textura fotográfica;
  prohibido texto de relleno tipo "Lorem ipsum" — todo el contenido debe ser real
  y relevante al pedido del usuario

REGLAS DE CONTENIDO (para que el docente pueda usarlo sin retocar nada):
- Generar contenido específico y completo según lo pedido, no genérico ni placeholder
- Textos breves y en español neutro, apropiados para 3-5 años (frases cortas, vocabulario simple)
- Revisar que ningún texto quede cortado por el contenedor (usar overflow-wrap/word-break)
- Si el pedido es ambiguo, completar con una interpretación razonable y pedagógicamente
  sensata, nunca dejar espacios vacíos o placeholders tipo "[texto aquí]"

ESTILO IMPRESIÓN (INCLUIR SIEMPRE, el recurso se imprime en A4):
- @page { size: A4; margin: 1.5cm; }
- El contenedor principal en pantalla también debe respetar proporción A4:
  max-width: 21cm; min-height: 29.7cm; margin: 0 auto;
- @media print obligatorio con:
  - body { margin: 0; padding: 0; background: white; }
  - Ocultar botones, navegación o cualquier elemento que no sea el recurso en sí
  - Mantener colores de fondo de tarjetas/bloques con
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
  - Evitar que un bloque se corte entre páginas: usar break-inside: avoid;
    en tarjetas, recuadros y áreas de actividad
  - Ajustar tamaños si hace falta para que TODO el contenido entre en la hoja

ESTRUCTURA HTML OBLIGATORIA:
- <!DOCTYPE html> completo, <html lang="es">, <head> con <meta charset="utf-8">
  y <meta name="viewport" content="width=device-width, initial-scale=1">
- Un único archivo HTML autocontenido: CSS dentro de <style>, JS (si hace falta)
  dentro de <script>, sin dependencias externas salvo Google Fonts
- Responsive mobile-first para la vista en pantalla, pero priorizando que en
  impresión (A4) se vea perfecto, que es el uso principal
- No dejar ```html ni ningún otro texto fuera de las etiquetas <html>...</html>
"""

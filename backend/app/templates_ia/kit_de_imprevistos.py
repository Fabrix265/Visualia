KIT_DE_IMPREVISTOS_INSTRUCCIONES = """
INSTRUCCIONES ESPECÍFICAS PARA KIT DE IMPREVISTOS:

Qué es: un único archivo que contiene VARIAS mini-actividades independientes ya
resueltas, para que la docente elija una con un solo toque en el momento en que
algo se rompe en la clase (un niño llora, sobra tiempo, el grupo perdió la
atención, hay que hacer una transición). No se genera nada nuevo en el momento:
todo el contenido ya está escrito y lo único que pasa "en vivo" es mostrar/ocultar
con JavaScript la sección elegida. Es HTML/CSS/JS autocontenido, sin llamadas a
ningún servidor ni a internet.

Estructura requerida:
1. PANTALLA DE INICIO (menú): una grilla de 4 a 5 botones grandes, cada uno con
   un ícono y una etiqueta corta que indica QUÉ TIPO de imprevisto resuelve, por ejemplo:
   - "Recuperar la atención" (un juego relámpago tipo "Simón dice" de 30-60 segundos)
   - "Calmar al grupo" (una respiración guiada animada, con un círculo que crece/decrece)
   - "Llenar 5 minutos" (una actividad corta de conteo o adivinanza)
   - "Pedir silencio" (una señal visual grande, ej. semáforo que cambia a rojo)
   - "Festejar un logro" (una animación breve de aplausos/estrellas)
   El docente puede pedir un tema (ej. "kit de imprevistos de animales de la
   granja"): en ese caso, ambientar el contenido de cada módulo con ese tema,
   sin perder la función de cada uno.
2. CADA MÓDULO es una sección propia (un <div> o pantalla) con:
   - Contenido ya completo y listo para usar (texto/instrucción breve + animación
     o elemento visual), sin que la docente tenga que escribir nada
   - Un botón "← Volver al menú" bien visible, siempre en el mismo lugar

Reglas técnicas de interactividad:
- Todo dentro de un solo archivo HTML: cada módulo es un <div id="modulo-x">
  oculto por defecto (display:none), el menú es el único visible al cargar
- Los botones del menú, al tocarse, ocultan el menú y muestran el módulo
  correspondiente con JavaScript simple (sin frameworks, sin dependencias externas)
- Las animaciones (respiración, estrellas, semáforo) se hacen con CSS
  (@keyframes) o JS mínimo, nunca con librerías externas ni video
- Cada módulo debe poder usarse repetidas veces sin recargar la página

Características obligatorias:
- Pensado para pantalla (no para imprimir): usar todo el viewport, tipografía
  grande (mínimo 24px), botones táctiles grandes (mínimo 64px de alto)
- Máximo 1-2 colores pastel de fondo por módulo, para que se distinga uno de otro
- Nada de texto largo: cada módulo se entiende de un vistazo, sin leer instrucciones
- El botón de volver al menú siempre debe estar disponible; nunca dejar un
  módulo como un callejón sin salida
"""

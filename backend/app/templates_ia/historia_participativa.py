HISTORIA_PARTICIPATIVA_INSTRUCCIONES = """
INSTRUCCIONES ESPECÍFICAS PARA HISTORIA PARTICIPATIVA:

Qué es: un cuento corto e ilustrado que la docente lee o muestra al grupo, y
que en 2 o 3 momentos clave se detiene para que TODO el grupo decida en voz
alta (levantando la mano) qué pasa después, entre 2 opciones. La docente toca
la opción que ganó la votación y la historia continúa por esa rama, con su
propio texto e ilustración. Es un único archivo HTML/CSS/JS: todas las ramas
ya están escritas de antemano, no hay generación en el momento.

Estructura requerida:
1. PORTADA/INICIO: título del cuento + una ilustración SVG grande del
   personaje o escenario principal + un botón grande "Empezar"
2. TRAMO DE HISTORIA (se repite en cada nodo del árbol):
   - Texto breve (2-4 oraciones simples, apropiadas para 3-5 años) que avanza
     la historia
   - Una ilustración SVG grande relacionada con ese momento del cuento
   - Al llegar a un punto de decisión: una pregunta corta ("¿Qué hace el
     oso?") con 2 botones grandes, cada uno con ícono + texto muy corto
     (2-4 palabras) para cada opción
3. ÁRBOL DE RAMAS: la historia debe tener 2 puntos de decisión, generando en
   total 4 finales distintos posibles (2 decisiones x 2 opciones cada una) —
   cada rama con su propio texto e ilustración, coherente con las decisiones
   tomadas antes
4. FINAL: cada uno de los 4 finales cierra la historia con una moraleja o
   cierre breve, y un botón "Volver a empezar" para poder jugarla de nuevo
   eligiendo otras opciones

Reglas técnicas de interactividad:
- Un solo archivo HTML: cada tramo de la historia (portada, nodos intermedios,
  finales) es un <div> propio, oculto por defecto salvo la portada
- Cada botón de opción, al tocarse, oculta el tramo actual y muestra el
  siguiente tramo correspondiente a esa rama, con JavaScript simple
  (si/else o mostrar por id), sin frameworks ni dependencias externas
- El botón "Volver a empezar" reinicia la vista a la portada (mostrar portada,
  ocultar el resto), permitiendo rejugar sin recargar la página

Características obligatorias:
- Pensado para pantalla/proyección: tipografía grande y legible a distancia,
  ilustraciones grandes, botones de decisión con mínimo 56px de alto
- Las 4 ramas deben ser igual de válidas y interesantes entre sí (ninguna
  opción debe sentirse "la correcta" ni las otras como error o castigo)
- Historia y decisiones apropiadas para 3-5 años: sin conflicto violento,
  con causa-efecto simple y entendible
- Nada de texto largo por pantalla: cada tramo se lee en 10-15 segundos como
  máximo, priorizando la ilustración sobre el texto
"""

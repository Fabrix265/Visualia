CLASIFICADOR_INTERACTIVO_INSTRUCCIONES = """
INSTRUCCIONES ESPECÍFICAS PARA CLASIFICADOR INTERACTIVO:

Qué es: un juego donde el niño clasifica elementos tocándolos y asignándolos
a la categoría correcta (ej: animales por hábitat, alimentos por tipo, formas
por color), sobre el tema que pida la docente. Trabaja una habilidad de
pre-matemática clave a esta edad: agrupar por atributo. HTML/CSS/JS
autocontenido, sin conexión ni backend.

Mecánica de interacción (IMPORTANTE): NO usar drag-and-drop nativo del
navegador (eventos dragstart/drop) — es poco confiable en pantallas táctiles
dentro de un iframe. Usar en cambio el patrón "tocar y tocar":
1. El niño toca UN elemento de la bandeja (queda resaltado/seleccionado)
2. Después toca UNA categoría → si el elemento pertenece a esa categoría,
   se mueve ahí con una animación simple y feedback positivo (✓, color
   verde, un pequeño rebote); si no pertenece, el elemento vuelve a la
   bandeja sin castigo, solo puede reintentar con otra categoría

Estructura requerida:
1. PORTADA: título del juego + consigna corta ("Tocá cada animal y llevalo
   a su hábitat") + botón "Empezar"
2. BANDEJA DE ELEMENTOS: 6 a 9 elementos (íconos/SVG grandes) desordenados,
   arriba o al costado de la pantalla
3. CATEGORÍAS: 2 o 3 categorías bien diferenciadas por color e ícono, como
   zonas grandes en la parte inferior de la pantalla
4. Al clasificar todos los elementos correctamente: pantalla de festejo
   simple (✓ grande, mensaje corto) + botón "Jugar de nuevo"

Características obligatorias:
- Elementos y categorías con áreas táctiles grandes (mínimo 64px)
- Máximo 2-3 categorías y 6-9 elementos por juego, para que sea abarcable
  de un vistazo por un niño de 3-5 años
- Un elemento debe pertenecer siempre a UNA sola categoría correcta, sin
  ambigüedad
- El JS debe llevar el estado de: elemento seleccionado actualmente, qué
  elementos ya se clasificaron bien, y detectar cuándo están todos
  clasificados para mostrar la pantalla de festejo — todo con variables
  simples y sin librerías externas
"""

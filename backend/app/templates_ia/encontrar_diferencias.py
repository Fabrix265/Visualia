ENCONTRAR_DIFERENCIAS_INSTRUCCIONES = """
INSTRUCCIONES ESPECÍFICAS PARA ENCONTRAR LAS DIFERENCIAS:

Qué es: un juego con dos escenas casi idénticas (relacionadas al tema que
pida la docente), con 3 a 4 diferencias escondidas que el niño debe tocar
para encontrar. Trabaja atención sostenida y discriminación visual.
HTML/CSS/JS autocontenido, sin conexión ni backend.

Estructura requerida:
1. PORTADA: título + consigna corta ("Encontrá las diferencias en la
   escena de la granja") + botón "Empezar"
2. PANTALLA DE JUEGO:
   - Dos escenas SVG simples, una al lado de la otra (o una arriba de la
     otra en pantallas angostas), que se ven casi iguales
   - 3 a 4 diferencias reales entre ambas (un elemento que cambia de color,
     que aparece en una escena y no en la otra, que cambia de tamaño o
     posición) — deben ser diferencias claramente visibles para un niño de
     3-5 años, nunca sutiles al punto de frustrar
   - Un contador arriba ("Encontraste 0 de 4")
   - Al tocar una diferencia correcta: se marca con un círculo o resaltado
     y sube el contador; tocar la misma zona de nuevo no debe sumar dos veces
   - Tocar una zona sin diferencia no penaliza, simplemente no pasa nada
3. Al encontrar las 4: pantalla de festejo + botón "Jugar de nuevo"

Características obligatorias:
- Las diferencias deben poder tocarse con un área táctil generosa alrededor
  del elemento real (no exigir precisión de píxel)
- Escenas simples y con pocos elementos (evitar escenas muy detalladas
  donde sea difícil ubicarse) — priorizar 6 a 10 elementos totales por escena
- El JS debe llevar el estado de: qué diferencias ya se encontraron (para
  no sumar dos veces la misma) y el contador — variables simples, sin
  librerías externas
- Nada de límite de tiempo ni penalización por intentos fallidos
"""

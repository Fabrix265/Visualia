SECUENCIA_LOGICA_INSTRUCCIONES = """
INSTRUCCIONES ESPECÍFICAS PARA SECUENCIA LÓGICA:

Qué es: un juego donde el niño ordena 3 a 4 imágenes de un proceso (el ciclo
de una semilla, los pasos para lavarse las manos, el día y la noche) tocándolas
en el orden correcto. Trabaja secuenciación y causa-efecto sobre el tema que
pida la docente. HTML/CSS/JS autocontenido, sin conexión ni backend.

Mecánica de interacción: "tocar para colocar en el próximo lugar libre"
(no usar drag-and-drop nativo, por la misma razón que en otros juegos: poco
confiable en táctil dentro de un iframe):
1. Arriba, una fila de 3-4 casilleros vacíos numerados (1, 2, 3, 4)
2. Abajo, las mismas 3-4 imágenes pero DESORDENADAS, en una bandeja
3. El niño toca una imagen de la bandeja → se coloca automáticamente en el
   próximo casillero vacío de arriba (en el orden en que las va tocando)
4. Cuando los 4 casilleros están llenos, aparece un botón "Revisar"
5. Al tocar "Revisar": si el orden es correcto, festejo (✓ + mensaje);
   si no, las imágenes vuelven a la bandeja (con una animación suave, sin
   mensaje de error duro) para que el niño intente de nuevo

Estructura requerida:
1. PORTADA: título + consigna corta ("Ordená los pasos para lavarte las
   manos") + botón "Empezar"
2. PANTALLA DE JUEGO: casilleros arriba, bandeja de imágenes abajo, botón
   "Revisar" (deshabilitado hasta llenar todos los casilleros)
3. PANTALLA FINAL (al acertar): mensaje de festejo + botón "Jugar de nuevo"

Características obligatorias:
- Imágenes/ilustraciones en SVG simple o emoji grande, con un tamaño
  uniforme entre todas
- Áreas táctiles grandes (mínimo 64px) para cada imagen y casillero
- Un solo proceso por juego, de 3 a 4 pasos — nunca más, para que sea
  abarcable a esta edad
- El JS debe llevar el estado de: qué casilleros están ocupados y con qué
  imagen, y validar el orden correcto al tocar "Revisar" — variables simples,
  sin librerías externas
- Nunca frustrar: reintentar debe ser instantáneo y sin penalización
"""

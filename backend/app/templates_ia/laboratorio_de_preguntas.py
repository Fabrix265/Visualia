LABORATORIO_DE_PREGUNTAS_INSTRUCCIONES = """
INSTRUCCIONES ESPECÍFICAS PARA LABORATORIO DE PREGUNTAS:

Qué es: una mini-trivia de 4 a 5 preguntas sobre el tema que pida la docente,
pensada como cierre de una actividad o clase, para que la docente vea en el
momento si el grupo entendió el tema. Da feedback inmediato en cada pregunta
y un resultado final. Es HTML/CSS/JS autocontenido, sin conexión ni backend.

Estructura requerida:
1. PORTADA: título del laboratorio + un botón grande "Empezar"
2. UNA PREGUNTA POR PANTALLA (4 a 5 en total):
   - Indicador de progreso arriba ("Pregunta 2 de 5")
   - La pregunta en texto simple, con un ícono/SVG grande relacionado si ayuda
   - 2 o 3 opciones de respuesta como botones grandes (nunca más de 3)
   - Al tocar una opción: marcarla con feedback inmediato y claro —
     verde + ✓ si es correcta, o de otro color suave + una marca (no rojo
     agresivo) si no lo es, mostrando además cuál era la correcta
   - Botón "Siguiente" que aparece recién después de responder esa pregunta
3. PANTALLA FINAL: puntaje total ("Acertaste 4 de 5") con un mensaje siempre
   alentador (nunca punitivo, incluso con puntaje bajo — el foco es repasar,
   no calificar) + botón "Jugar de nuevo"

Reglas de feedback (importante, es el corazón de este recurso):
- El feedback debe ser inmediato: apenas se toca una opción, sin esperar a
  terminar todas las preguntas
- Nunca dejar que el niño quede sin saber si acertó o no
- El mensaje final siempre motiva a seguir aprendiendo, independientemente
  del puntaje (nunca "mal", "reprobado" ni comparaciones)
- Se puede tocar una sola opción por pregunta; una vez respondida esa
  pregunta, las demás opciones quedan deshabilitadas (no se puede cambiar
  la respuesta ya marcada)

Características obligatorias:
- Pensado para pantalla (tablet en mano del niño, o turnos frente a la
  pantalla con ayuda de la docente): botones táctiles de mínimo 56px de alto
- Preguntas y opciones cortas, en una sola línea si es posible
- Ilustraciones en SVG simple o emoji grande, nunca fotos realistas
- El JS debe manejar: número de pregunta actual, cuál se respondió, contador
  de aciertos — todo con variables simples, sin librerías externas
"""

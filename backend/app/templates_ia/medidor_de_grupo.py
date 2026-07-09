MEDIDOR_DE_GRUPO_INSTRUCCIONES = """
INSTRUCCIONES ESPECÍFICAS PARA MEDIDOR DE GRUPO:

Qué es: un recurso que "se adapta" al ritmo del grupo sin que la docente tenga
que generar nada nuevo. Es un único archivo HTML/CSS/JS con un control visual
(dial, termómetro o 3 botones grandes) con 3 estados posibles del grupo:
"disperso", "cansado" y "enganchado". Al tocar cada estado, el mismo archivo
muestra una actividad distinta ya escrita de antemano sobre el mismo tema
pedido por la docente. Todo el contenido de los 3 estados se genera de una
sola vez; en el momento de usarlo no hay conexión a internet ni IA, solo
JavaScript local mostrando/ocultando contenido.

Estructura requerida:
1. SELECTOR DE ESTADO: arriba de todo, 3 botones grandes y claramente
   diferenciados por color e ícono:
   - 😵 "Disperso" — el grupo no presta atención
   - 😴 "Cansado" — el grupo está bajo de energía
   - 🤩 "Enganchado" — el grupo está atento y quiere más
2. TRES ACTIVIDADES (una por estado), todas sobre el mismo tema que pida la
   docente, cada una en su propio <div> oculto hasta que se elige su estado:
   - Para "disperso": una actividad corta y muy dinámica para recuperar
     la atención (un "seguime"/Simón dice de 30 segundos, relacionado al tema)
   - Para "cansado": una actividad calma y de baja energía sobre el mismo
     tema (respiración guiada, observar algo, escuchar una pista relacionada)
   - Para "enganchado": una versión más desafiante o extendida de la
     actividad original sobre el tema (una pregunta más difícil, un paso más)
3. El estado seleccionado debe quedar visualmente resaltado (borde o fondo
   distinto) para que la docente sepa en qué modo está parada

Reglas técnicas de interactividad:
- Un solo archivo HTML: los 3 bloques de actividad son <div> ocultos por
  defecto salvo uno inicial (sugerido: "enganchado" como estado por defecto)
- Los botones de selección de estado alternan la visibilidad de los 3 <div>
  con JavaScript simple, sin recargar la página ni pedir nada al servidor
- Se puede cambiar de estado ida y vuelta las veces que haga falta durante
  la clase

Características obligatorias:
- Pensado para pantalla (proyección o tablet en mano de la docente): tipografía
  grande, alto contraste, botones táctiles de al menos 56px de alto
- Las 3 actividades deben sentirse conectadas al mismo tema pedido, no
  actividades sueltas sin relación entre sí
- Nada de texto largo en ninguna de las 3 variantes: instrucciones de una
  sola frase, el resto es la actividad en sí (íconos, elementos para señalar,
  preguntas cortas)
"""

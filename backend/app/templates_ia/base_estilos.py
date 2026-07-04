BASE_ESTILOS = """
REGLAS DE ESTILO OBLIGATORIAS (aplicar SIEMPRE):

COLORES:
- Fondo general: blanco crema (#FFFDF7)
- Barra superior: azul pastel (#AEE2FF)
- Botones: verde menta (#B8F2D0), lila pastel (#E2D6F3), durazno pastel (#FFDAB9)
- Favoritos: rosa pastel (#FFD1E3)
- Tarjetas: rotar entre azul (#AEE2FF), rosa (#FFD1E3), lila (#E2D6F3), verde (#B8F2D0) pastel
- Texto principal: oscuro suave (#333333)

TIPOGRAFÍA:
- Encabezados/branding: Fredoka (estilo infantil, redondeada)
- Textos generales: Nunito o Quicksand
- Cargar vía Google Fonts en el HTML

ESTILO VISUAL:
- Bordes redondeados en todo (border-radius: 16-24px)
- Íconos grandes y amigables (mínimo 32-40px en botones principales)
- Mucho espacio en blanco, layouts poco saturados
- Jerarquía visual clara
- Sombras muy sutiles (box-shadow suave, sin bordes duros)
- Nada de imágenes realistas o agresivas

ESTILO IMPRESIÓN (INCLUIR SIEMPRE):
- Agregar @media print con:
  - body { margin: 0; padding: 0; background: white; }
  - @page { margin: 1.5cm; size: A4; }
  - Ocultar botones, navegación, elementos no esenciales
  - Ajustar tamaños de fuente para impresión
  - Evitar cortes de contenido entre páginas
  - Mantener colores de fondo para tarjetas (usar -webkit-print-color-adjust: exact)

ESTRUCTURA HTML:
- Documento HTML completo y autocontenido
- CSS inline o en <style>
- Google Fonts cargado vía <link>
- Responsive (mobile-first)
"""

import TopBar from '../components/TopBar'
import BotonPrimario from '../components/BotonPrimario'
import TarjetaRecurso from '../components/TarjetaRecurso'
import VisorRecurso from '../components/VisorRecurso'

const recursosEjemplo = [
  { id: 1, titulo: 'Ficha de colores', tipo: 'ficha', origen: 'propio', es_favorito: true },
  { id: 2, titulo: 'Hoja gráfica de números', tipo: 'hoja_grafica', origen: 'compartido', compartido_por: 'María', es_favorito: false },
  { id: 3, titulo: 'Afiche de seguridad', tipo: 'afiche', origen: 'propio', es_favorito: false },
  { id: 4, titulo: 'Lámina de animales', tipo: 'lamina', origen: 'propio', es_favorito: true },
]

const htmlEjemplo = `
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: 'Fredoka', sans-serif; text-align: center; padding: 20px; background: #f0f9ff; }
    h1 { color: #4a5568; }
    .emoji { font-size: 48px; }
  </style>
</head>
<body>
  <div class="emoji">🎨</div>
  <h1>Recurso de Ejemplo</h1>
  <p>Este es un contenido generado por IA</p>
</body>
</html>
`

export default function Componentes() {
  return (
    <div className="min-h-screen bg-gray-50">
      <TopBar />
      
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-fredoka text-center mb-8">Catálogo de Componentes</h1>
        
        {/* TopBar */}
        <section className="mb-12">
          <h2 className="text-2xl font-fredoka mb-4">TopBar</h2>
          <p className="text-gray-600 mb-4">Barra superior con logo y navegación</p>
        </section>

        {/* Botones */}
        <section className="mb-12">
          <h2 className="text-2xl font-fredoka mb-4">Botones</h2>
          <div className="flex flex-wrap gap-4">
            <BotonPrimario variante="generar">Generar</BotonPrimario>
            <BotonPrimario variante="descargar">Descargar</BotonPrimario>
            <BotonPrimario variante="imprimir">Imprimir</BotonPrimario>
            <BotonPrimario variante="primario">Primario</BotonPrimario>
            <BotonPrimario variante="secundario">Secundario</BotonPrimario>
            <BotonPrimario variante="peligro">Peligro</BotonPrimario>
            <BotonPrimario disabled>Deshabilitado</BotonPrimario>
          </div>
        </section>

        {/* Tarjetas */}
        <section className="mb-12">
          <h2 className="text-2xl font-fredoka mb-4">Tarjetas de Recurso</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
            {recursosEjemplo.map((recurso, index) => (
              <TarjetaRecurso key={recurso.id} recurso={recurso} index={index} />
            ))}
          </div>
        </section>

        {/* Visor */}
        <section className="mb-12">
          <h2 className="text-2xl font-fredoka mb-4">Visor de Recurso</h2>
          <VisorRecurso htmlContent={htmlEjemplo} />
        </section>
      </div>
    </div>
  )
}

import { Link, useNavigate } from 'react-router-dom'
import TopBar from '../components/TopBar'

const tiposRecurso = [
  { tipo: 'ficha', nombre: 'Ficha', icono: '📄', color: 'bg-pastel-blue' },
  { tipo: 'hoja_grafica', nombre: 'Hoja gráfica', icono: '📝', color: 'bg-pastel-pink' },
  { tipo: 'afiche', nombre: 'Afiche', icono: '🖼️', color: 'bg-pastel-purple' },
  { tipo: 'lamina', nombre: 'Lámina', icono: '🎨', color: 'bg-pastel-green' },
]

export default function Inicio() {
  const navigate = useNavigate()

  const handleTipoClick = (tipo) => {
    navigate(`/crear?tipo=${tipo}`)
  }

  return (
    <div className="min-h-screen bg-cream">
      <TopBar />
      
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-fredoka text-center mb-8">¿Qué querés crear?</h1>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-2xl mx-auto">
          {tiposRecurso.map((item) => (
            <button
              key={item.tipo}
              onClick={() => handleTipoClick(item.tipo)}
              className={`${item.color} rounded-2xl p-8 shadow-md hover:shadow-lg transition-shadow duration-200 cursor-pointer text-left`}
            >
              <span className="text-5xl">{item.icono}</span>
              <h2 className="mt-4 text-2xl font-fredoka text-gray-800">{item.nombre}</h2>
            </button>
          ))}
        </div>

        <div className="mt-12 text-center">
          <Link
            to="/mis-recursos"
            className="text-sky-600 font-nunito font-semibold hover:underline"
          >
            Ver mis recursos →
          </Link>
        </div>
      </div>
    </div>
  )
}

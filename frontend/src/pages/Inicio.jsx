import { Link, useNavigate } from 'react-router-dom'
import TopBar from '../components/TopBar'

const tiposRecurso = [
  { tipo: 'ficha', nombre: 'Ficha', descripcion: 'Para que un niño trabaje solo', icono: '📄', color: 'bg-pastel-blue' },
  { tipo: 'hoja_grafica', nombre: 'Hoja gráfica', descripcion: 'Actividad visual, casi sin texto', icono: '📝', color: 'bg-pastel-pink' },
  { tipo: 'afiche', nombre: 'Afiche', descripcion: 'Para pegar en la pared del aula', icono: '🖼️', color: 'bg-pastel-purple' },
  { tipo: 'lamina', nombre: 'Lámina', descripcion: 'Para mostrar a todo el grupo', icono: '🎨', color: 'bg-pastel-green' },
  { tipo: 'pictograma', nombre: 'Pictograma', descripcion: 'Texto con íconos en lugar de palabras', icono: '🔤', color: 'bg-pastel-yellow' },
  { tipo: 'instructivo', nombre: 'Instructivo', descripcion: 'Guía paso a paso con materiales', icono: '📋', color: 'bg-pastel-orange' },
]

export default function Inicio() {
  const navigate = useNavigate()

  const handleTipoClick = (tipo) => {
    navigate(`/crear?tipo=${tipo}`)
  }

  return (
    <div className="min-h-screen bg-cream">
      <TopBar />

      <div className="container mx-auto px-4 py-8 sm:py-12 animar-entrada">
        <h1 className="text-2xl sm:text-3xl font-fredoka font-semibold text-center mb-1">¿Qué querés crear?</h1>
        <p className="text-ink/60 text-center mb-8">Elegí un tipo de recurso para empezar</p>

        <div className="grid grid-cols-2 gap-3 sm:gap-5 max-w-2xl mx-auto">
          {tiposRecurso.map((item) => (
            <button
              key={item.tipo}
              onClick={() => handleTipoClick(item.tipo)}
              className={`tocable ${item.color} rounded-3xl p-5 sm:p-7 shadow-soft hover:shadow-soft-md cursor-pointer text-left flex flex-col items-start gap-2 sm:gap-3`}
            >
              <span className="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-white/60 flex items-center justify-center text-2xl sm:text-3xl">
                {item.icono}
              </span>
              <div>
                <h2 className="font-fredoka font-semibold text-lg sm:text-xl text-ink">{item.nombre}</h2>
                <p className="text-xs sm:text-sm text-ink/60 mt-0.5 leading-snug">{item.descripcion}</p>
              </div>
            </button>
          ))}
        </div>

        <div className="mt-10 flex justify-center">
          <Link
            to="/mis-recursos"
            className="inline-flex items-center gap-2 bg-white px-5 py-3 rounded-2xl shadow-soft hover:shadow-soft-md font-nunito font-bold text-ink transition-all"
          >
            Ver mis recursos <span aria-hidden="true">→</span>
          </Link>
        </div>
      </div>
    </div>
  )
}

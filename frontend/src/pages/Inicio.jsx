import { Link, useNavigate } from 'react-router-dom'
import TopBar from '../components/TopBar'

const recursosPrevios = [
  { tipo: 'ficha', nombre: 'Ficha', descripcion: 'Para que un niño trabaje solo', icono: '📄', color: 'bg-pastel-blue' },
  { tipo: 'hoja_grafica', nombre: 'Hoja gráfica', descripcion: 'Actividad visual, casi sin texto', icono: '📝', color: 'bg-pastel-pink' },
  { tipo: 'lamina', nombre: 'Lámina', descripcion: 'Para mostrar a todo el grupo', icono: '🎨', color: 'bg-pastel-green' },
  { tipo: 'instructivo', nombre: 'Instructivo', descripcion: 'Guía paso a paso con materiales', icono: '📋', color: 'bg-pastel-orange' },
]

const recursosEnVivo = [
  { tipo: 'kit_de_imprevistos', nombre: 'Kit de imprevistos', descripcion: 'Mini-actividades para usar en el momento', icono: '🧰', color: 'bg-pastel-blue' },
  { tipo: 'medidor_de_grupo', nombre: 'Medidor de grupo', descripcion: 'Se adapta al ritmo del grupo con un toque', icono: '📊', color: 'bg-pastel-pink' },
  { tipo: 'historia_participativa', nombre: 'Historia participativa', descripcion: 'Cuento interactivo que decide el grupo', icono: '📖', color: 'bg-pastel-purple' },
]

const juegosInteractivos = [
  { tipo: 'laboratorio_de_preguntas', nombre: 'Laboratorio de preguntas', descripcion: 'Mini-trivia con feedback y puntaje', icono: '❓', color: 'bg-pastel-yellow' },
  { tipo: 'clasificador_interactivo', nombre: 'Clasificador interactivo', descripcion: 'Agrupar elementos por categoría', icono: '🗂️', color: 'bg-pastel-green' },
  { tipo: 'secuencia_logica', nombre: 'Secuencia lógica', descripcion: 'Ordenar los pasos de un proceso', icono: '🔢', color: 'bg-pastel-orange' },
  { tipo: 'encontrar_diferencias', nombre: 'Encontrá las diferencias', descripcion: 'Juego de atención entre dos escenas', icono: '🔍', color: 'bg-pastel-purple' },
]

function SeccionRecursos({ titulo, items, onTipoClick }) {
  return (
    <div className="mb-10">
      <h2 className="font-fredoka font-semibold text-ink/70 text-sm uppercase tracking-wide mb-3 px-1">
        {titulo}
      </h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 sm:gap-5">
        {items.map((item) => (
          <button
            key={item.tipo}
            onClick={() => onTipoClick(item.tipo)}
            className={`tocable ${item.color} rounded-3xl p-5 sm:p-6 shadow-soft hover:shadow-soft-md cursor-pointer text-left flex flex-col items-start gap-2 sm:gap-3`}
          >
            <span className="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-white/60 flex items-center justify-center text-2xl sm:text-3xl">
              {item.icono}
            </span>
            <div>
              <h3 className="font-fredoka font-semibold text-lg sm:text-xl text-ink">{item.nombre}</h3>
              <p className="text-xs sm:text-sm text-ink/60 mt-0.5 leading-snug">{item.descripcion}</p>
            </div>
          </button>
        ))}
      </div>
    </div>
  )
}

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

        <div className="max-w-3xl mx-auto">
          <SeccionRecursos
            titulo="Para preparar antes de la clase"
            items={recursosPrevios}
            onTipoClick={handleTipoClick}
          />
          <SeccionRecursos
            titulo="Para usar durante la clase"
            items={recursosEnVivo}
            onTipoClick={handleTipoClick}
          />
          <SeccionRecursos
            titulo="Juegos interactivos de aprendizaje"
            items={juegosInteractivos}
            onTipoClick={handleTipoClick}
          />
        </div>

        <div className="mt-2 flex justify-center">
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

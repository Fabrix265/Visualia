import { Link } from 'react-router-dom'

const colores = [
  'bg-pastel-blue',
  'bg-pastel-pink',
  'bg-pastel-purple',
  'bg-pastel-green',
]

const iconos = {
  ficha: '📄',
  hoja_grafica: '📝',
  afiche: '🖼️',
  lamina: '🎨',
}

export default function TarjetaRecurso({ recurso, index = 0 }) {
  const colorFondo = colores[index % colores.length]
  const icono = iconos[recurso.tipo] || '📄'

  return (
    <Link to={`/recurso/${recurso.id}`}>
      <div className={`${colorFondo} rounded-2xl p-4 shadow-md hover:shadow-lg transition-shadow duration-200 cursor-pointer`}>
        <div className="flex items-start justify-between">
          <div className="text-3xl">{icono}</div>
          {recurso.es_favorito && (
            <span className="text-pink-400 text-xl">★</span>
          )}
        </div>
        <h3 className="mt-2 font-fredoka text-lg text-gray-800 truncate">{recurso.titulo}</h3>
        <p className="text-sm text-gray-600 capitalize">{recurso.tipo.replace('_', ' ')}</p>
        {recurso.origen === 'compartido' && (
          <p className="text-xs text-gray-500 mt-1">
            Compartido por {recurso.compartido_por}
          </p>
        )}
      </div>
    </Link>
  )
}

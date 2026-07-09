import { Link } from 'react-router-dom'

const colores = [
  'bg-pastel-blue',
  'bg-pastel-pink',
  'bg-pastel-purple',
  'bg-pastel-green',
  'bg-pastel-yellow',
  'bg-pastel-orange',
]

const iconos = {
  ficha: '📄',
  hoja_grafica: '📝',
  afiche: '🖼️',
  lamina: '🎨',
  pictograma: '🔤',
  instructivo: '📋',
}

export default function TarjetaRecurso({ recurso, index = 0 }) {
  const colorFondo = colores[index % colores.length]
  const icono = iconos[recurso.tipo] || '📄'

  return (
    <Link to={`/recurso/${recurso.id}`} className="block h-full">
      <div className="tocable relative h-full bg-white rounded-2xl p-4 shadow-soft hover:shadow-soft-md cursor-pointer border border-black/5">
        {recurso.es_favorito && (
          <span
            className="absolute -top-2 -right-2 w-7 h-7 flex items-center justify-center rounded-full bg-pastel-pink text-ink text-sm shadow-soft"
            aria-label="Favorito"
          >
            ★
          </span>
        )}

        <div className={`${colorFondo} w-12 h-12 rounded-xl flex items-center justify-center text-2xl mb-3`}>
          {icono}
        </div>

        <h3 className="font-fredoka font-semibold text-base text-ink recorte-2">{recurso.titulo}</h3>
        <p className="text-sm text-ink/60 capitalize mt-0.5">{recurso.tipo.replace('_', ' ')}</p>

        {recurso.origen === 'compartido' && (
          <p className="text-xs text-ink/50 mt-2 truncate">
            Compartido por {recurso.compartido_por}
          </p>
        )}
      </div>
    </Link>
  )
}

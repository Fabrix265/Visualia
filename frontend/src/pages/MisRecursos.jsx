import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import client from '../api/client'
import TopBar from '../components/TopBar'
import TarjetaRecurso from '../components/TarjetaRecurso'
import Cargando from '../components/Cargando'

const tiposFiltro = [
  { valor: '', etiqueta: 'Todos' },
  { valor: 'ficha', etiqueta: 'Fichas' },
  { valor: 'hoja_grafica', etiqueta: 'Hojas gráficas' },
  { valor: 'afiche', etiqueta: 'Afiches' },
  { valor: 'lamina', etiqueta: 'Láminas' },
  { valor: 'pictograma', etiqueta: 'Pictogramas' },
  { valor: 'instructivo', etiqueta: 'Instructivos' },
  { valor: 'kit_de_imprevistos', etiqueta: 'Kits de imprevistos' },
  { valor: 'medidor_de_grupo', etiqueta: 'Medidores de grupo' },
  { valor: 'historia_participativa', etiqueta: 'Historias participativas' },
  { valor: 'laboratorio_de_preguntas', etiqueta: 'Laboratorios de preguntas' },
  { valor: 'clasificador_interactivo', etiqueta: 'Clasificadores' },
  { valor: 'secuencia_logica', etiqueta: 'Secuencias lógicas' },
  { valor: 'encontrar_diferencias', etiqueta: 'Encontrá las diferencias' },
]

export default function MisRecursos() {
  const [recursos, setRecursos] = useState([])
  const [cargando, setCargando] = useState(true)
  const [filtroTipo, setFiltroTipo] = useState('')
  const [soloFavoritos, setSoloFavoritos] = useState(false)

  useEffect(() => {
    cargarRecursos()
  }, [filtroTipo, soloFavoritos])

  const cargarRecursos = async () => {
    setCargando(true)
    let url = '/recursos/mis-recursos?'
    if (filtroTipo) url += `tipo=${filtroTipo}&`
    if (soloFavoritos) url += 'es_favorito=true'

    const { data } = await client(url)
    if (data) {
      setRecursos(data)
    }
    setCargando(false)
  }

  return (
    <div className="min-h-screen bg-cream">
      <TopBar showBack title="Mis recursos" />

      <div className="container mx-auto px-4 py-8 animar-entrada">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-2xl sm:text-3xl font-fredoka font-semibold">Mis recursos</h1>
          <Link
            to="/"
            className="bg-pastel-green text-ink px-4 py-2.5 rounded-2xl shadow-soft hover:shadow-soft-md hover:brightness-95 active:scale-95 transition-all font-nunito font-bold text-sm sm:text-base"
          >
            + Crear
          </Link>
        </div>

        <div className="flex flex-wrap items-center gap-2 mb-6">
          {tiposFiltro.map((f) => (
            <button
              key={f.valor}
              onClick={() => setFiltroTipo(f.valor)}
              className={`px-4 py-2 rounded-full text-sm font-nunito font-bold transition-all cursor-pointer ${
                filtroTipo === f.valor
                  ? 'bg-pastel-blue text-ink shadow-soft'
                  : 'bg-white text-ink/60 border border-black/10 hover:bg-cream'
              }`}
            >
              {f.etiqueta}
            </button>
          ))}

          <button
            onClick={() => setSoloFavoritos(!soloFavoritos)}
            className={`flex items-center gap-1.5 px-4 py-2 rounded-full text-sm font-nunito font-bold transition-all cursor-pointer ${
              soloFavoritos
                ? 'bg-pastel-pink text-ink shadow-soft'
                : 'bg-white text-ink/60 border border-black/10 hover:bg-cream'
            }`}
          >
            <span aria-hidden="true">★</span> Favoritos
          </button>
        </div>

        {cargando ? (
          <Cargando mensaje="Cargando recursos..." />
        ) : recursos.length === 0 ? (
          <div className="text-center py-16">
            <div className="w-16 h-16 mx-auto rounded-full bg-white flex items-center justify-center text-3xl mb-4 shadow-soft">
              🗂️
            </div>
            <p className="text-ink/60 mb-4 font-nunito">No tenés recursos todavía</p>
            <Link
              to="/"
              className="inline-block bg-pastel-green text-ink px-6 py-3 rounded-2xl shadow-soft hover:shadow-soft-md hover:brightness-95 active:scale-95 transition-all font-nunito font-bold"
            >
              Crear mi primer recurso
            </Link>
          </div>
        ) : (
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3 sm:gap-4">
            {recursos.map((recurso, index) => (
              <TarjetaRecurso key={recurso.id} recurso={recurso} index={index} />
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

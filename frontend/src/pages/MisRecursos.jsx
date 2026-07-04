import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import client from '../api/client'
import TopBar from '../components/TopBar'
import TarjetaRecurso from '../components/TarjetaRecurso'

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
    <div className="min-h-screen bg-gray-50">
      <TopBar />
      
      <div className="container mx-auto px-4 py-8">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-3xl font-fredoka">Mis recursos</h1>
          <Link
            to="/"
            className="bg-pastel-green text-white px-4 py-2 rounded-xl hover:bg-green-400 transition-colors"
          >
            + Crear
          </Link>
        </div>

        <div className="flex flex-wrap gap-3 mb-6">
          <select
            value={filtroTipo}
            onChange={(e) => setFiltroTipo(e.target.value)}
            className="px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:border-pastel-blue"
          >
            <option value="">Todos los tipos</option>
            <option value="ficha">Fichas</option>
            <option value="hoja_grafica">Hojas gráficas</option>
            <option value="afiche">Afiches</option>
            <option value="lamina">Láminas</option>
          </select>

          <label className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={soloFavoritos}
              onChange={(e) => setSoloFavoritos(e.target.checked)}
              className="w-4 h-4 rounded border-gray-300 text-pink-400 focus:ring-pink-400"
            />
            <span className="text-gray-700 font-nunito">Solo favoritos</span>
          </label>
        </div>

        {cargando ? (
          <p className="text-gray-500 text-center py-8">Cargando recursos...</p>
        ) : recursos.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500 mb-4">No tenés recursos todavía</p>
            <Link
              to="/"
              className="bg-pastel-green text-white px-6 py-3 rounded-xl hover:bg-green-400 transition-colors"
            >
              Crear mi primer recurso
            </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {recursos.map((recurso, index) => (
              <TarjetaRecurso key={recurso.id} recurso={recurso} index={index} />
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

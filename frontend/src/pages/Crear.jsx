import { useState } from 'react'
import { useSearchParams, useNavigate } from 'react-router-dom'
import client from '../api/client'
import TopBar from '../components/TopBar'
import BotonPrimario from '../components/BotonPrimario'

export default function Crear() {
  const [searchParams] = useSearchParams()
  const tipo = searchParams.get('tipo') || 'ficha'
  const navigate = useNavigate()

  const [titulo, setTitulo] = useState('')
  const [prompt, setPrompt] = useState('')
  const [modoProyeccion, setModoProyeccion] = useState(false)
  const [cargando, setCargando] = useState(false)
  const [error, setError] = useState('')

  const nombresTipo = {
    ficha: 'Ficha',
    hoja_grafica: 'Hoja gráfica',
    afiche: 'Afiche',
    lamina: 'Lámina',
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setCargando(true)

    const { data, error: apiError } = await client('/recursos/generar', {
      method: 'POST',
      body: {
        tipo,
        titulo,
        prompt_usuario: prompt,
        modo_proyeccion: modoProyeccion,
      },
    })

    setCargando(false)

    if (apiError) {
      setError(apiError)
      return
    }

    navigate(`/recurso/${data.id}`)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <TopBar />
      
      <div className="container mx-auto px-4 py-8 max-w-2xl">
        <h1 className="text-3xl font-fredoka text-center mb-2">
          Crear {nombresTipo[tipo]}
        </h1>
        <p className="text-gray-600 text-center mb-8">
          Describí lo que querés generar con IA
        </p>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-xl mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 font-nunito mb-2">Título</label>
            <input
              type="text"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              placeholder="Ej: Ficha de colores primarios"
              className="w-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:border-pastel-green"
              required
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-700 font-nunito mb-2">Descripción del recurso</label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Ej: Una ficha para que los niños identifiquen los colores primarios, con imágenes grandes y espacios para colorear"
              className="w-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:border-pastel-green h-32 resize-none"
              required
            />
          </div>

          <div className="mb-6">
            <label className="flex items-center gap-3 cursor-pointer">
              <input
                type="checkbox"
                checked={modoProyeccion}
                onChange={(e) => setModoProyeccion(e.target.checked)}
                className="w-5 h-5 rounded border-gray-300 text-pastel-green focus:ring-pastel-green"
              />
              <span className="text-gray-700 font-nunito">
                ¿Este recurso será proyectado?
              </span>
            </label>
            <p className="text-sm text-gray-500 mt-1 ml-8">
              Se optimiza para verse en pantalla grande
            </p>
          </div>

          <BotonPrimario type="submit" variante="generar" className="w-full" disabled={cargando}>
            {cargando ? '✨ Generando tu recurso...' : 'Generar recurso'}
          </BotonPrimario>
        </form>
      </div>
    </div>
  )
}

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
    lamina: 'Lámina',
    instructivo: 'Instructivo',
    kit_de_imprevistos: 'Kit de imprevistos',
    medidor_de_grupo: 'Medidor de grupo',
    historia_participativa: 'Historia participativa',
    laboratorio_de_preguntas: 'Laboratorio de preguntas',
    clasificador_interactivo: 'Clasificador interactivo',
    secuencia_logica: 'Secuencia lógica',
    encontrar_diferencias: 'Encontrá las diferencias',
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
    <div className="min-h-screen bg-cream">
      <TopBar showBack title={`Crear ${nombresTipo[tipo]}`} />

      <div className="container mx-auto px-4 py-8 max-w-xl animar-entrada">
        <h1 className="text-2xl sm:text-3xl font-fredoka font-semibold text-center mb-2">
          Crear {nombresTipo[tipo]}
        </h1>
        <p className="text-ink/60 text-center mb-8">
          Describí lo que querés generar con IA
        </p>

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-2xl mb-4 text-sm font-nunito">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="bg-white rounded-3xl shadow-soft p-5 sm:p-7">
          <div className="mb-5">
            <label className="block text-ink font-nunito font-bold text-sm mb-2">Título</label>
            <input
              type="text"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              placeholder="Ej: Ficha de colores primarios"
              className="w-full px-4 py-3 rounded-2xl border border-black/10 bg-cream/60 focus:outline-none focus:border-pastel-green focus:bg-white transition-colors"
              required
            />
          </div>

          <div className="mb-5">
            <label className="block text-ink font-nunito font-bold text-sm mb-2">Descripción del recurso</label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Ej: Una ficha para que los niños identifiquen los colores primarios, con imágenes grandes y espacios para colorear"
              className="w-full px-4 py-3 rounded-2xl border border-black/10 bg-cream/60 focus:outline-none focus:border-pastel-green focus:bg-white transition-colors h-32 resize-none"
              required
            />
          </div>

          <label className="flex items-center justify-between gap-3 cursor-pointer bg-cream/60 rounded-2xl px-4 py-3 mb-6">
            <span>
              <span className="block text-ink font-nunito font-bold text-sm">¿Se va a proyectar?</span>
              <span className="block text-xs text-ink/50 mt-0.5">Se optimiza para pantalla grande</span>
            </span>
            <span className="relative inline-flex shrink-0">
              <input
                type="checkbox"
                checked={modoProyeccion}
                onChange={(e) => setModoProyeccion(e.target.checked)}
                className="peer sr-only"
              />
              <span className="w-12 h-7 rounded-full bg-black/15 peer-checked:bg-pastel-green transition-colors"></span>
              <span className="absolute top-1 left-1 w-5 h-5 rounded-full bg-white shadow-soft transition-transform peer-checked:translate-x-5"></span>
            </span>
          </label>

          <BotonPrimario type="submit" variante="generar" className="w-full" disabled={cargando}>
            {cargando ? '✨ Generando tu recurso...' : 'Generar recurso'}
          </BotonPrimario>
        </form>
      </div>
    </div>
  )
}

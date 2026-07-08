import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import client from '../api/client'
import TopBar from '../components/TopBar'
import VisorRecurso from '../components/VisorRecurso'
import BotonPrimario from '../components/BotonPrimario'
import Cargando from '../components/Cargando'
import Error from '../components/Error'
import { descargarHTML, imprimirHTML } from '../utils/archivos'

export default function RecursoDetalle() {
  const { id } = useParams()
  const navigate = useNavigate()
  const [recurso, setRecurso] = useState(null)
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')
  const [busqueda, setBusqueda] = useState('')
  const [resultadosBusqueda, setResultadosBusqueda] = useState([])
  const [mostrarBuscador, setMostrarBuscador] = useState(false)
  const [copiado, setCopiado] = useState(false)

  useEffect(() => {
    cargarRecurso()
  }, [id])

  const cargarRecurso = async () => {
    const { data, error: apiError } = await client(`/recursos/${id}`)
    setCargando(false)
    if (apiError) {
      setError(apiError)
      return
    }
    setRecurso(data)
  }

  const toggleFavorito = async () => {
    const { data } = await client(`/recursos/${id}/favorito`, {
      method: 'PATCH',
    })
    if (data) {
      setRecurso({ ...recurso, es_favorito: data.es_favorito })
    }
  }

  const buscarDocentes = async (q) => {
    if (q.length < 2) {
      setResultadosBusqueda([])
      return
    }
    const { data } = await client(`/docentes/buscar?q=${q}`)
    if (data) {
      setResultadosBusqueda(data)
    }
  }

  const compartirConDocente = async (docenteId) => {
    const { error: apiError } = await client(`/recursos/${id}/compartir-con-docente?docente_destino_id=${docenteId}`, {
      method: 'POST',
    })
    if (!apiError) {
      setMostrarBuscador(false)
      setBusqueda('')
      setResultadosBusqueda([])
    }
  }

  const copiarEnlace = async () => {
    const { data } = await client(`/recursos/${id}/enlace-publico`, {
      method: 'POST',
    })
    if (data) {
      const url = `${window.location.origin}/compartido/${data.token}`
      navigator.clipboard.writeText(url)
      setCopiado(true)
      setTimeout(() => setCopiado(false), 2000)
    }
  }

  const eliminarRecurso = async () => {
    if (!confirm('¿Estás seguro de eliminar este recurso?')) return
    const { error: apiError } = await client(`/recursos/${id}`, {
      method: 'DELETE',
    })
    if (!apiError) {
      navigate('/mis-recursos')
    }
  }

  if (cargando) {
    return (
      <div className="min-h-screen bg-cream">
        <TopBar showBack />
        <Cargando mensaje="Cargando recurso..." />
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-cream">
        <TopBar showBack />
        <Error mensaje={error} onReintentar={cargarRecurso} />
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-cream">
      <TopBar showBack />

      <div className="container mx-auto px-4 py-8 max-w-4xl animar-entrada">
        <div className="flex items-center justify-between gap-3 mb-6">
          <h1 className="text-2xl sm:text-3xl font-fredoka font-semibold truncate">{recurso.titulo}</h1>
          {recurso.origen === 'compartido' && (
            <span className="shrink-0 text-xs sm:text-sm text-ink/60 bg-white px-3 py-1.5 rounded-full shadow-soft">
              Compartido por {recurso.compartido_por}
            </span>
          )}
        </div>

        <VisorRecurso htmlContent={recurso.html_content} modoProyeccion={recurso.modo_proyeccion} />

        <div className="mt-6 flex flex-wrap gap-2.5">
          <BotonPrimario
            variante={recurso.es_favorito ? 'favorito' : 'secundario'}
            onClick={toggleFavorito}
          >
            {recurso.es_favorito ? '★ Favorito' : '☆ Favorito'}
          </BotonPrimario>

          {recurso.origen === 'propio' && (
            <>
              <BotonPrimario variante="secundario" onClick={() => setMostrarBuscador(true)}>
                Compartir con docente
              </BotonPrimario>
              <BotonPrimario variante="descargar" onClick={copiarEnlace}>
                {copiado ? '¡Copiado!' : 'Copiar enlace público'}
              </BotonPrimario>
              <BotonPrimario variante="descargar" onClick={() => descargarHTML(recurso.html_content, recurso.titulo)}>
                Descargar
              </BotonPrimario>
              <BotonPrimario variante="imprimir" onClick={() => imprimirHTML(recurso.html_content)}>
                Imprimir
              </BotonPrimario>
              <BotonPrimario variante="peligro" onClick={eliminarRecurso}>
                Eliminar
              </BotonPrimario>
            </>
          )}
        </div>

        {mostrarBuscador && (
          <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-3xl p-6 w-full max-w-md shadow-soft-lg animar-entrada">
              <h2 className="text-xl font-fredoka font-semibold mb-4">Compartir con docente</h2>
              <input
                type="text"
                value={busqueda}
                onChange={(e) => {
                  setBusqueda(e.target.value)
                  buscarDocentes(e.target.value)
                }}
                placeholder="Buscar por nombre..."
                className="w-full px-4 py-3 rounded-2xl border border-black/10 bg-cream/60 focus:outline-none focus:border-pastel-blue focus:bg-white transition-colors mb-4"
                autoFocus
              />
              <div className="max-h-60 overflow-y-auto -mx-1">
                {resultadosBusqueda.map((docente) => (
                  <button
                    key={docente.id}
                    onClick={() => compartirConDocente(docente.id)}
                    className="w-full text-left px-4 py-3 hover:bg-cream rounded-2xl transition-colors font-nunito cursor-pointer"
                  >
                    {docente.nombre}
                  </button>
                ))}
              </div>
              <button
                onClick={() => setMostrarBuscador(false)}
                className="mt-4 w-full text-center text-ink/50 hover:text-ink font-nunito transition-colors cursor-pointer"
              >
                Cancelar
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

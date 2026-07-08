import { useState, useEffect, useRef } from 'react'
import { useParams } from 'react-router-dom'
import client from '../api/client'

export default function CompartidoPublico() {
  const { token } = useParams()
  const [recurso, setRecurso] = useState(null)
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')
  const iframeRef = useRef(null)

  useEffect(() => {
    cargarRecurso()
  }, [token])

  const cargarRecurso = async () => {
    const { data, error: apiError } = await client(`/compartido/${token}`)
    setCargando(false)
    if (apiError) {
      setError(apiError)
      return
    }
    setRecurso(data)
  }

  const handleFullscreen = () => {
    if (iframeRef.current) {
      if (iframeRef.current.requestFullscreen) {
        iframeRef.current.requestFullscreen()
      } else if (iframeRef.current.webkitRequestFullscreen) {
        iframeRef.current.webkitRequestFullscreen()
      }
    }
  }

  if (cargando) {
    return (
      <div className="min-h-screen bg-cream flex items-center justify-center">
        <div className="flex flex-col items-center gap-3">
          <div className="spinner-marca rounded-full h-10 w-10 border-4 border-pastel-blue border-t-transparent"></div>
          <p className="text-ink/60 font-nunito font-semibold">Cargando recurso...</p>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-cream flex items-center justify-center px-4">
        <div className="text-center max-w-sm">
          <div className="w-16 h-16 mx-auto rounded-full bg-pastel-orange/60 flex items-center justify-center text-3xl mb-4">
            😕
          </div>
          <p className="text-red-500 font-nunito font-bold mb-2">{error}</p>
          <p className="text-ink/50 text-sm">El enlace no es válido o el recurso fue eliminado</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-white">
      <iframe
        ref={iframeRef}
        srcDoc={recurso.html_content}
        sandbox="allow-scripts"
        className="w-full h-screen border-0"
        title={recurso.titulo}
      />
      <button
        onClick={handleFullscreen}
        className="fixed bottom-4 right-4 flex items-center gap-2 bg-pastel-blue text-ink px-5 py-3 rounded-2xl shadow-soft-md hover:brightness-95 active:scale-95 transition-all z-50 font-nunito font-bold cursor-pointer"
      >
        <span aria-hidden="true">⛶</span> Pantalla completa
      </button>
    </div>
  )
}

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
      <div className="min-h-screen bg-white flex items-center justify-center">
        <p className="text-gray-500 font-nunito">Cargando recurso...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-white flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-500 font-nunito mb-4">{error}</p>
          <p className="text-gray-500">El enlace no es válido o el recurso fue eliminado</p>
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
        className="fixed bottom-4 right-4 bg-pastel-blue text-white px-4 py-2 rounded-2xl shadow-md hover:brightness-95 transition-all z-50 text-ink font-nunito font-semibold cursor-pointer"
      >
        Pantalla completa
      </button>
    </div>
  )
}

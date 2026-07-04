import { useRef } from 'react'

export default function VisorRecurso({ htmlContent, modoProyeccion = false }) {
  const iframeRef = useRef(null)

  const handleFullscreen = () => {
    if (iframeRef.current) {
      if (iframeRef.current.requestFullscreen) {
        iframeRef.current.requestFullscreen()
      } else if (iframeRef.current.webkitRequestFullscreen) {
        iframeRef.current.webkitRequestFullscreen()
      }
    }
  }

  if (modoProyeccion) {
    return (
      <div className="relative w-full h-screen">
        <iframe
          ref={iframeRef}
          srcDoc={htmlContent}
          sandbox="allow-scripts"
          className="w-full h-full border-0"
          title="Recurso para proyección"
        />
        <button
          onClick={handleFullscreen}
          className="absolute bottom-4 right-4 bg-pastel-blue text-white px-4 py-2 rounded-2xl shadow-md hover:bg-blue-400 transition-colors"
        >
          Pantalla completa
        </button>
      </div>
    )
  }

  return (
    <div className="w-full rounded-2xl overflow-hidden shadow-md border border-gray-200">
      <iframe
        ref={iframeRef}
        srcDoc={htmlContent}
        sandbox="allow-scripts"
        className="w-full h-96 border-0"
        title="Vista previa del recurso"
      />
    </div>
  )
}

import { useRef } from 'react'

export default function VisorRecurso({ htmlContent, modoProyeccion = false }) {
  const iframeRef = useRef(null)

  const handleFullscreen = () => {
    const el = iframeRef.current
    if (!el) return
    if (el.requestFullscreen) {
      el.requestFullscreen()
    } else if (el.webkitRequestFullscreen) {
      el.webkitRequestFullscreen()
    }
  }

  if (modoProyeccion) {
    return (
      <div className="relative w-full h-[70vh] sm:h-screen rounded-2xl overflow-hidden shadow-md">
        <iframe
          ref={iframeRef}
          srcDoc={htmlContent}
          sandbox="allow-scripts"
          className="w-full h-full border-0 bg-white"
          title="Recurso para proyección"
        />
        <button
          onClick={handleFullscreen}
          className="absolute bottom-4 right-4 bg-pastel-blue text-white px-4 py-2 rounded-2xl shadow-md hover:brightness-95 transition-all font-nunito font-semibold cursor-pointer"
        >
          ⛶ Pantalla completa
        </button>
      </div>
    )
  }

  return (
    <div className="relative w-full rounded-2xl overflow-hidden shadow-md border border-black/5">
      <iframe
        ref={iframeRef}
        srcDoc={htmlContent}
        sandbox="allow-scripts"
        className="w-full h-[60vh] min-h-96 border-0 bg-white"
        title="Vista previa del recurso"
      />
      <button
        onClick={handleFullscreen}
        className="absolute bottom-3 right-3 bg-white/90 backdrop-blur px-3 py-2 rounded-2xl shadow-md hover:bg-white transition-all font-nunito font-semibold text-sm cursor-pointer"
      >
        ⛶ Ver completo
      </button>
    </div>
  )
}

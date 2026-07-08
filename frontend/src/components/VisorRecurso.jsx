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
      <div className="relative w-full h-[70vh] sm:h-screen rounded-2xl overflow-hidden shadow-soft-lg border border-black/5">
        <iframe
          ref={iframeRef}
          srcDoc={htmlContent}
          sandbox="allow-scripts"
          className="w-full h-full border-0 bg-white"
          title="Recurso para proyección"
        />
        <button
          onClick={handleFullscreen}
          className="absolute bottom-4 right-4 flex items-center gap-2 bg-pastel-blue text-ink px-5 py-3 rounded-2xl shadow-soft-md hover:brightness-95 active:scale-95 transition-all font-nunito font-bold cursor-pointer"
        >
          <span aria-hidden="true">⛶</span> Proyectar en pantalla completa
        </button>
      </div>
    )
  }

  return (
    <div className="relative w-full rounded-2xl overflow-hidden shadow-soft border border-black/5">
      <iframe
        ref={iframeRef}
        srcDoc={htmlContent}
        sandbox="allow-scripts"
        className="w-full h-[60vh] min-h-96 border-0 bg-white"
        title="Vista previa del recurso"
      />
      <button
        onClick={handleFullscreen}
        className="absolute bottom-3 right-3 flex items-center gap-1.5 bg-white/90 backdrop-blur px-3 py-2 rounded-2xl shadow-soft hover:bg-white active:scale-95 transition-all font-nunito font-bold text-sm cursor-pointer"
      >
        <span aria-hidden="true">⛶</span> Ver completo
      </button>
    </div>
  )
}

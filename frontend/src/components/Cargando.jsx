export default function Cargando({ mensaje = 'Cargando...' }) {
  return (
    <div className="flex flex-col items-center justify-center py-16 animar-entrada">
      <div className="spinner-marca rounded-full h-12 w-12 border-4 border-pastel-blue border-t-transparent mb-4"></div>
      <p className="text-ink/60 font-nunito font-semibold">{mensaje}</p>
    </div>
  )
}

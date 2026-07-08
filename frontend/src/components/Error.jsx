import BotonPrimario from './BotonPrimario'

export default function Error({ mensaje = 'Algo salió mal', onReintentar }) {
  return (
    <div className="flex flex-col items-center justify-center py-16 text-center animar-entrada">
      <div className="w-16 h-16 rounded-full bg-pastel-orange/60 flex items-center justify-center text-3xl mb-4">
        😕
      </div>
      <p className="text-ink/70 font-nunito font-semibold mb-4 max-w-xs">{mensaje}</p>
      {onReintentar && (
        <BotonPrimario variante="primario" onClick={onReintentar}>
          Reintentar
        </BotonPrimario>
      )}
    </div>
  )
}

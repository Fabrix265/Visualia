import BotonPrimario from './BotonPrimario'

export default function Error({ mensaje = 'Algo salió mal', onReintentar }) {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className="text-6xl mb-4"> :( </div>
      <p className="text-gray-600 font-nunito mb-4">{mensaje}</p>
      {onReintentar && (
        <BotonPrimario variante="primario" onClick={onReintentar}>
          Reintentar
        </BotonPrimario>
      )}
    </div>
  )
}

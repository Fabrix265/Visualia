const variants = {
  generar: 'bg-pastel-green hover:bg-green-400 text-white',
  descargar: 'bg-pastel-purple hover:bg-purple-400 text-white',
  imprimir: 'bg-pastel-orange hover:bg-orange-400 text-white',
  primario: 'bg-pastel-blue hover:bg-blue-400 text-white',
  secundario: 'bg-gray-200 hover:bg-gray-300 text-gray-700',
  peligro: 'bg-red-400 hover:bg-red-500 text-white',
}

export default function BotonPrimario({ children, variante = 'primario', className = '', disabled = false, onClick, type = 'button' }) {
  const baseStyles = 'px-6 py-3 rounded-2xl font-nunito font-semibold shadow-md transition-all duration-200 ease-in-out cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed'
  const variantStyles = variants[variante] || variants.primario

  return (
    <button
      type={type}
      className={`${baseStyles} ${variantStyles} ${className}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  )
}

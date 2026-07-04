const variants = {
  generar: 'bg-pastel-green text-ink',
  descargar: 'bg-pastel-purple text-ink',
  imprimir: 'bg-pastel-orange text-ink',
  primario: 'bg-pastel-blue text-ink',
  secundario: 'bg-white text-ink border border-black/10',
  favorito: 'bg-pastel-pink text-ink',
  peligro: 'bg-white text-red-500 border border-red-200',
}

export default function BotonPrimario({ children, variante = 'primario', className = '', disabled = false, onClick, type = 'button' }) {
  const baseStyles = 'px-6 py-3 rounded-2xl font-nunito font-semibold shadow-sm hover:shadow-md hover:brightness-95 active:brightness-90 transition-all duration-200 ease-in-out cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:brightness-100'
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

import { Link, useNavigate } from 'react-router-dom'

/**
 * Barra superior reutilizable.
 * - showBack: muestra flecha para volver a la pantalla anterior.
 * - title: título centrado (si no se pasa, muestra el logo "Visualia").
 * - showLogout: muestra el botón de cerrar sesión (oculto en pantallas públicas).
 */
export default function TopBar({ showBack = false, title = null, showLogout = true }) {
  const navigate = useNavigate()

  const cerrarSesion = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <nav className="safe-top bg-pastel-blue/95 backdrop-blur-sm shadow-soft sticky top-0 z-40">
      <div className="container mx-auto px-3 sm:px-4 py-3 flex items-center gap-2">
        <div className="flex-1 flex items-center gap-2 min-w-0">
          {showBack && (
            <button
              onClick={() => navigate(-1)}
              aria-label="Volver"
              className="w-11 h-11 shrink-0 flex items-center justify-center rounded-full bg-white/50 hover:bg-white/80 active:scale-95 text-2xl leading-none text-ink transition-all cursor-pointer"
            >
              ←
            </button>
          )}

          {title ? (
            <h1 className="font-fredoka font-semibold text-lg sm:text-xl text-ink truncate">{title}</h1>
          ) : (
            <Link to="/" className="flex items-center gap-2">
              <span className="text-2xl font-fredoka font-semibold text-ink">Visualia</span>
            </Link>
          )}
        </div>

        {showLogout && (
          <button
            onClick={cerrarSesion}
            aria-label="Cerrar sesión"
            className="shrink-0 flex items-center gap-1.5 h-11 px-4 rounded-full bg-white/50 hover:bg-white/80 active:scale-95 text-ink text-sm font-nunito font-bold transition-all cursor-pointer"
          >
            <span aria-hidden="true">⏻</span>
            <span className="hidden sm:inline">Salir</span>
          </button>
        )}
      </div>
    </nav>
  )
}

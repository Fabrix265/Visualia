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
    <nav className="bg-pastel-blue shadow-sm sticky top-0 z-40">
      <div className="container mx-auto px-3 py-3 flex items-center gap-2">
        <div className="flex-1 flex items-center gap-2 min-w-0">
          {showBack && (
            <button
              onClick={() => navigate(-1)}
              aria-label="Volver"
              className="w-10 h-10 shrink-0 flex items-center justify-center rounded-full bg-white/40 hover:bg-white/70 text-2xl leading-none text-white transition-colors cursor-pointer"
            >
              ←
            </button>
          )}

          {title ? (
            <h1 className="font-fredoka text-lg sm:text-xl text-white truncate">{title}</h1>
          ) : (
            <Link to="/" className="flex items-center gap-2">
              <span className="text-2xl font-fredoka text-white">Visualia</span>
            </Link>
          )}
        </div>

        {showLogout && (
          <button
            onClick={cerrarSesion}
            aria-label="Cerrar sesión"
            className="shrink-0 flex items-center gap-1.5 px-3 py-2 rounded-full bg-white/40 hover:bg-white/70 text-white text-sm font-nunito font-semibold transition-colors cursor-pointer"
          >
            <span aria-hidden="true">⏻</span>
            <span className="hidden sm:inline">Salir</span>
          </button>
        )}
      </div>
    </nav>
  )
}

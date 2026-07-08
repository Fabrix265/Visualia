import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import client from '../api/client'
import BotonPrimario from '../components/BotonPrimario'

export default function Login() {
  const [nombre, setNombre] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [cargando, setCargando] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setCargando(true)

    const { data, error: apiError, status } = await client('/auth/login', {
      method: 'POST',
      body: { nombre, password },
    })

    setCargando(false)

    if (apiError) {
      setError(status === 401 ? 'Nombre o contraseña incorrectos' : apiError)
      return
    }

    localStorage.setItem('token', data.token)
    navigate('/')
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-pastel-blue px-4">
      <div className="bg-white p-6 sm:p-8 rounded-3xl shadow-soft-lg w-full max-w-md animar-entrada">
        <div className="text-center mb-6">
          <span className="text-3xl font-fredoka font-semibold text-ink">Visualia</span>
          <h1 className="text-xl font-fredoka font-semibold text-ink/80 mt-1">Iniciar sesión</h1>
        </div>

        {error && (
          <div className="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-2xl mb-4 text-sm font-nunito">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-ink font-nunito font-bold text-sm mb-2">Nombre</label>
            <input
              type="text"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              className="w-full px-4 py-3 rounded-2xl border border-black/10 bg-cream/60 focus:outline-none focus:border-pastel-blue focus:bg-white transition-colors"
              required
            />
          </div>

          <div className="mb-6">
            <label className="block text-ink font-nunito font-bold text-sm mb-2">Contraseña</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-2xl border border-black/10 bg-cream/60 focus:outline-none focus:border-pastel-blue focus:bg-white transition-colors"
              required
            />
          </div>

          <BotonPrimario type="submit" variante="generar" className="w-full" disabled={cargando}>
            {cargando ? 'Ingresando...' : 'Ingresar'}
          </BotonPrimario>
        </form>

        <p className="text-center mt-6 text-ink/60 text-sm">
          ¿No tenés cuenta?{' '}
          <Link to="/registro" className="text-ink font-bold hover:underline">
            Registrate
          </Link>
        </p>
      </div>
    </div>
  )
}

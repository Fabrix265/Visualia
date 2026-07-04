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
    <div className="min-h-screen flex items-center justify-center bg-pastel-blue">
      <div className="bg-white p-8 rounded-2xl shadow-lg w-full max-w-md">
        <h1 className="text-3xl font-fredoka text-center mb-6">Iniciar Sesión</h1>
        
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-xl mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 font-nunito mb-2">Nombre</label>
            <input
              type="text"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:border-pastel-blue"
              required
            />
          </div>

          <div className="mb-6">
            <label className="block text-gray-700 font-nunito mb-2">Contraseña</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:border-pastel-blue"
              required
            />
          </div>

          <BotonPrimario type="submit" variante="generar" className="w-full" disabled={cargando}>
            {cargando ? 'Ingresando...' : 'Ingresar'}
          </BotonPrimario>
        </form>

        <p className="text-center mt-6 text-gray-600">
          ¿No tenés cuenta?{' '}
          <Link to="/registro" className="text-pastel-blue hover:underline">
            Registrate
          </Link>
        </p>
      </div>
    </div>
  )
}

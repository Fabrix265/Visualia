import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Registro from './pages/Registro'
import Inicio from './pages/Inicio'
import Crear from './pages/Crear'
import MisRecursos from './pages/MisRecursos'
import RecursoDetalle from './pages/RecursoDetalle'
import CompartidoPublico from './pages/CompartidoPublico'
import Componentes from './pages/Componentes'
import ProtectedRoute from './components/ProtectedRoute'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/registro" element={<Registro />} />
        <Route path="/compartido/:token" element={<CompartidoPublico />} />
        <Route path="/componentes" element={<Componentes />} />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Inicio />
            </ProtectedRoute>
          }
        />
        <Route
          path="/crear"
          element={
            <ProtectedRoute>
              <Crear />
            </ProtectedRoute>
          }
        />
        <Route
          path="/mis-recursos"
          element={
            <ProtectedRoute>
              <MisRecursos />
            </ProtectedRoute>
          }
        />
        <Route
          path="/recurso/:id"
          element={
            <ProtectedRoute>
              <RecursoDetalle />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App

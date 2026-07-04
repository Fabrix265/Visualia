import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Registro from './pages/Registro'
import Inicio from './pages/Inicio'
import Crear from './pages/Crear'
import MisRecursos from './pages/MisRecursos'
import RecursoDetalle from './pages/RecursoDetalle'
import CompartidoPublico from './pages/CompartidoPublico'
import Componentes from './pages/Componentes'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/registro" element={<Registro />} />
        <Route path="/" element={<Inicio />} />
        <Route path="/crear" element={<Crear />} />
        <Route path="/mis-recursos" element={<MisRecursos />} />
        <Route path="/recurso/:id" element={<RecursoDetalle />} />
        <Route path="/compartido/:token" element={<CompartidoPublico />} />
        <Route path="/componentes" element={<Componentes />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App

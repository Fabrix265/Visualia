import { Link } from 'react-router-dom'

export default function TopBar() {
  return (
    <nav className="bg-pastel-blue shadow-md">
      <div className="container mx-auto px-4 py-3">
        <Link to="/" className="flex items-center justify-center gap-2">
          <span className="text-2xl font-fredoka text-white">Visualia</span>
        </Link>
      </div>
    </nav>
  )
}

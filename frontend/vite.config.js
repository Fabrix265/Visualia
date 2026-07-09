import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: 5173,
    proxy: {
      '/auth': 'http://localhost:8000',
      '/recursos': 'http://localhost:8000',
      '/compartido': 'http://localhost:8000',
      '/docentes': 'http://localhost:8000',
    }
  }
})

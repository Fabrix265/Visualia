const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function client(endpoint, { body, ...customConfig } = {}) {
  const token = localStorage.getItem('token')

  const headers = {
    'Content-Type': 'application/json',
    ...customConfig.headers,
  }

  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  const config = {
    method: body ? 'POST' : 'GET',
    ...customConfig,
    headers,
  }

  if (body) {
    config.body = JSON.stringify(body)
  }

  try {
    const response = await fetch(`${API_URL}${endpoint}`, config)
    const data = await response.json()

    if (!response.ok) {
      return { error: data.detail || 'Error desconocido', status: response.status }
    }

    return { data, status: response.status }
  } catch (error) {
    return { error: error.message, status: 500 }
  }
}

export default client

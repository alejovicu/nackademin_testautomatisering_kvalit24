const API_URL = "http://localhost:8000"

export async function api(path, method = 'GET', body = null, token = null) {
  const headers = { 'Content-Type': 'application/json' }
  if (token) headers['Authorization'] = `Bearer ${token}`

  const res = await fetch(`${API_URL}${path}`, {
    method,
    headers,
    body: body ? JSON.stringify(body) : null,
  })

  if (!res.ok) throw new Error(await res.text())
  return res.json()
}

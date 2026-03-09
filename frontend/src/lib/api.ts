import axios from 'axios'

const baseURL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL,
  withCredentials: true,
})

export function setAuthToken(token: string | null) {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`
  } else {
    delete api.defaults.headers.common['Authorization']
    console.log("Token not provided")
  }
}

// Add response interceptor to handle 401 and refresh token
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // If 401 Unauthorized, clear token and redirect to login
    if (error.response?.status === 401) {
      if (typeof window !== 'undefined') {
        localStorage.removeItem('auth_token')
        setAuthToken(null)
        console.log("Unauthorized redirected")
        // Optionally redirect to login (can be done via Next.js router in components)
      }
    }
    return Promise.reject(error)
  }
)

export default api

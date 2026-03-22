import { useState, useCallback, useEffect } from 'react'
import api, { setAuthToken } from '../api'
import { redirect } from 'next/dist/server/api-utils'

export interface AuthResponse {
  access: string
  refresh?: string
  user? : string
}

export function useAuth() {
  const [token, setToken] = useState<string | null>(() => {
    if (typeof window === 'undefined') return null
    return localStorage.getItem('auth_token')
  })
  const [isInitialized, setIsInitialized] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // Load token from localStorage on mount
  useEffect(() => {
    const savedToken = localStorage.getItem('auth_token')
    if (savedToken) {
      setToken(savedToken)
      setAuthToken(savedToken)
    }
    setIsInitialized(true)
  }, [])

  const login = useCallback(
    async (username: string, password: string) => {
      setIsLoading(true)
      setError(null)
      try {
        const { data } = await api.post<AuthResponse>('/auth/login/', {
          username,
          password,
        })
        const { access, user } = data
      //  console.log(user[0].id)
        localStorage.setItem('auth_token', access)
        localStorage.setItem('user_id', user[0].id)
        setAuthToken(access)
        setToken(access)
        
        return data
      } catch (err: any) {
        const message = err.response?.data?.detail || err.message || 'Login failed'
        setError(message)
        throw err
      } finally {
        setIsLoading(false)
      }
    },
    []
  )

  const register = useCallback(
    async (
      username: string,
      email: string,
      password: string,
      first_name?: string,
      last_name?: string
    ) => {
      setIsLoading(true)
      setError(null)
      try {
        const { data } = await api.post('/auth/register/', {
          username,
          email,
          password,
          first_name,
          last_name,
        })
        return data
      } catch (err: any) {
        const message = err.response?.data?.detail || err.message || 'Registration failed'
        setError(message)
        throw err
      } finally {
        setIsLoading(false)
      }
    },
    []
  )

  const logout = useCallback(() => {
    localStorage.removeItem('auth_token')
    setAuthToken(null)
    setToken(null)
    
  }, [])

  return {
    token,
    isAuthenticated: !!token,
    isInitialized,
    isLoading,
    error,
    login,
    register,
    logout,
  }
}

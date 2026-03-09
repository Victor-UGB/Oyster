'use client'

import { useAuth } from '@/lib/hooks/useAuth'
import { useRouter } from 'next/navigation'
import { useEffect } from 'react'
import AppBar from './AppBar'
import NavBar from './NavBar'

export function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isInitialized } = useAuth()
  const router = useRouter()

  useEffect(() => {
    if (isInitialized && !isAuthenticated) {
      router.push('/login')
    }
  }, [isAuthenticated, isInitialized, router])

  if (!isInitialized) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-lg text-gray-600">Checking session...</p>
      </div>
    )
  }

  if (!isAuthenticated) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-lg text-gray-600">Redirecting to login...</p>
      </div>
    )
  }

  return (
    <div>
      <div className='fixed w-full'><NavBar/></div>
      <>{children}</>
      <div className='fixed bottom-1 w-full'>
      <AppBar />
      </div>
    </div>
    )
}

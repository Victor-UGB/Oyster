'use client'

import { usePearls } from '@/lib/hooks/usePearls'
import Link from 'next/link'

export default function PearlsList() {
  const { data: pearls, isLoading, error } = usePearls()

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-lg text-gray-600">Loading pearls...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-lg text-red-600">Error loading pearls: {(error as Error).message}</p>
      </div>
    )
  }

  if (!pearls || pearls.length === 0) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-lg text-gray-600">No pearls found. Start creating one!</p>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4">
      <div className="container mx-auto max-w-4xl">
        <h1 className="text-4xl font-bold text-gray-800 mb-8">Your Pearls</h1>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {pearls.map((pearl) => (
            <Link
              key={pearl.id}
              href={`/pearl/${pearl.id}`}
              className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 cursor-pointer"
            >
              <div className="mb-4">
                <span className="inline-block px-3 py-1 text-xs font-semibold text-blue-700 bg-blue-100 rounded-full">
                  {pearl.content_type}
                </span>
              </div>

              <h2 className="text-xl font-bold text-gray-800 mb-2 line-clamp-2">
                {pearl.title || 'Untitled Pearl'}
              </h2>

              <p className="text-gray-600 text-sm mb-4 line-clamp-3">
                {pearl.content || pearl.url || 'No content'}
              </p>

              <div className="flex items-center justify-between text-xs text-gray-500">
                <span>{new Date(pearl.created_at).toLocaleDateString()}</span>
                <span className={pearl.is_public ? 'text-green-600' : 'text-gray-400'}>
                  {pearl.is_public ? '🌐 Public' : '🔒 Private'}
                </span>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}

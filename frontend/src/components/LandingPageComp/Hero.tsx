'use client'

import { useState, useEffect } from 'react'

interface HeroProps {}

const Hero: React.FC<HeroProps> = () => {
  const colors = ['#1f2937', '#dc2626', '#ea580c', '#7c3aed', '#16a34a'] // Tailwind colors
  const [count, setCount] = useState(0)
  const [bgColor, setBgColor] = useState(colors[0])

  useEffect(() => {
    const interval = setInterval(() => {
      setCount(prevCount => {
        const newCount = prevCount < 4 ? prevCount + 1 : 0
        setBgColor(colors[newCount])
        return newCount
      })
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div
      className="min-h-screen flex items-center justify-center transition-all duration-2000 ease-in-out"
      style={{ backgroundColor: bgColor }}
    >
      <div className="text-center text-white max-w-4xl mx-auto px-4">
        <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight">
          ONLY THE MOST BEAUTIFUL THINGS
        </h1>
        <p className="text-xl md:text-2xl mb-12 opacity-90">
          Share with the world the beauty of your world
        </p>

        <div className="max-w-md mx-auto">
          <form className="flex gap-2">
            <input
              type="text"
              placeholder="Type in anything"
              className="flex-1 px-4 py-3 rounded-lg text-gray-900 focus:outline-none focus:ring-2 focus:ring-white/50"
            />
            <button
              type="submit"
              className="px-6 py-3 bg-white text-gray-900 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
            >
              Search
            </button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default Hero
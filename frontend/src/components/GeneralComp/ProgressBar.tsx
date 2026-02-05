'use client'

import { useState, useEffect } from 'react'

interface ProgressBarProps {}

const ProgressBar: React.FC<ProgressBarProps> = () => {
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const onScroll = () => {
      const winScroll = document.documentElement.scrollTop
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight
      const scrolled = (winScroll / height) * 100

      setProgress(scrolled)
    }

    window.addEventListener('scroll', onScroll)

    return () => {
      window.removeEventListener('scroll', onScroll)
    }
  }, [])

  return (
    <div className="fixed top-0 left-0 right-0 z-40 h-1 bg-gray-200">
      <div
        className="h-full bg-primary-600 transition-all duration-150 ease-out"
        style={{ width: `${progress}%` }}
      />
    </div>
  )
}

export default ProgressBar
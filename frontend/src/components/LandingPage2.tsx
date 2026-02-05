'use client'

import { useState, useEffect } from 'react'
import Typewriter from 'typewriter-effect'
import Hero from './LandingPageComp/Hero'
import Navigation from './GeneralComp/Navigation'
import Card from './GeneralComp/Card'
import CardTwo from './GeneralComp/CardTwo'
import ProgressBar from './GeneralComp/ProgressBar'

interface LandingPageProps {}

const LandingPage: React.FC<LandingPageProps> = () => {
  const [count, setCount] = useState(0)
  const colors = ['black', 'red', 'orange', 'purple', 'green']

  const transitColor = () => {
    setCount(prevCount => (prevCount < 4 ? prevCount + 1 : 0))
  }

  useEffect(() => {
    const interval = setInterval(transitColor, 2000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <ProgressBar />
      <Navigation />

      {/* Hero Section */}
      <Hero />

      {/* Main Content */}
      <div className="container mx-auto px-4 py-16">
        <div className="text-center mb-16">
          <div className="text-4xl md:text-6xl font-bold text-gray-800 mb-6">
            <Typewriter
              onInit={(typewriter) => {
                typewriter
                  .typeString("The World is Your Community")
                  .pauseFor(2000)
                  .deleteAll()
                  .typeString("Do You")
                  .pauseFor(1000)
                  .deleteAll()
                  .typeString("Show Love")
                  .pauseFor(1000)
                  .deleteAll()
                  .typeString("Change Lives!")
                  .start()
              }}
            />
          </div>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Share the beauty of your world to a boundless community. Let people around the world into your beautiful mind.
          </p>
        </div>

        {/* Feature Cards */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <Card
            subTitle="Share Your Best"
            title="Now the world can hear from you"
            para="You can share thoughts and ideas and see how people benefit from them."
            actionBtn="Try for free"
            link="/login"
            btnClass="bg-primary-600 hover:bg-primary-700 text-white"
            imgSource="https://images.unsplash.com/photo-1544773088-d142e38f5793?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=813&q=80"
          />
          <Card
            subTitle="The Full Experience!"
            title="Share your ideas in text, sound and video"
            para="Give your viewers the full experience with the text, audio and video vblogs"
            actionBtn="Try for free"
            link="/login"
            btnClass="bg-primary-600 hover:bg-primary-700 text-white"
            imgSource="https://images.unsplash.com/photo-1593733925160-6f78dc0be8b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8aG9sZGluZyUyMHBob25lfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60"
          />
          <CardTwo
            subTitle="With Oyster"
            title=""
            para="Your creations are pearls. Be free to open up here."
            colorSwitch={colors[count]}
          />
        </div>

        {/* Call to Action */}
        <div className="text-center">
          <p className="text-2xl text-gray-700 font-medium">
            With Oyster, your creations are pearls. Be free to open up here.
          </p>
        </div>
      </div>
    </div>
  )
}

export default LandingPage
'use client'

// import LandingPage from '@/components/LandingPage'
import LandingPage from '@/components/LandingPage2'
import api from '@/lib/api'


export default function Home() {
  fetch(`${api}/pearl/list`)
  .then(
     
  )
  return <div>
    <div>Home</div>
    {/* <LandingPage /> */}
    
  </div>
}
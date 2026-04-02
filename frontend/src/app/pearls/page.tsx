import { UrlAiInput } from '@/components/AiComp/LLMComp/UrlAiInput'
import PearlsList from '@/components/PearlsList'
import { ProtectedRoute } from '@/components/ProtectedRoute'

export default function PearlsPage() {
  return (
    <ProtectedRoute>
      <PearlsList />
      
      <div className='sticky bottom-10'><UrlAiInput/></div>
    </ProtectedRoute>
  )
}

import PearlsList from '@/components/PearlsList'
import { ProtectedRoute } from '@/components/ProtectedRoute'

export default function PearlsPage() {
  return (
    <ProtectedRoute>
      <PearlsList />
    </ProtectedRoute>
  )
}

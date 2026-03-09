import { useQuery } from '@tanstack/react-query'
import api from '../api'

export interface Pearl {
  id: string
  title: string
  content: string | null
  content_type: string
  url: string | null
  is_public: boolean
  created_at: string
  updated_at: string
  pearl_image?: string | null
  pearl_audio?: string | null
  pearl_video?: string | null
  pearl_category?: string | null
  pearl_summary?: string | null
}

export function usePearls() {
  return useQuery({
    queryKey: ['pearls'],
    queryFn: async () => {
      const { data } = await api.get('/pearl/list/')
      // DRF returns paginated results by default
      if (Array.isArray(data)) {
        return data as Pearl[]
      }
      if (data && Array.isArray(data.results)) {
        return data.results as Pearl[]
      }
      // fallback empty array
      return [] as Pearl[]
    },
  })
}

export function usePearlDetail(id: string | string[]) {
  return useQuery({
    queryKey: ['pearl', id],
    queryFn: async () => {
      const { data } = await api.get<Pearl>(`/pearl/${id}/`)
      return data
    },
    enabled: !!id,
  })
}

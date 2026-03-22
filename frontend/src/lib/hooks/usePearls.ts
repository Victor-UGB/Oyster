import { useQuery } from '@tanstack/react-query'
import api from '../api'
import { useState, useCallback } from 'react'

export interface Pearl {
  id: string
  user: string
  title: string
  content: string | null
  content_type?: string
  url?: string | null
  is_public?: boolean
  created_at: string
  updated_at: string
  pearl_image?: string | null
  pearl_audio?: string | null
  pearl_video?: string | null
  pearl_category?: string | null
  pearl_summary?: string | null
}

export interface Tag {
  id: string,
  name: string,
  category: string,
  usage_count: number,
  created_at: string
}

export interface Folder {
  id: string,
  name: string,
  description: string,
  is_auto_generated: boolean,
  created_at: string,
  updated_at: string,
  user: string,
  parent: string
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

export function usePearlActions(){
  const [data, setData] = useState([])
  const [error, setError] = useState<string | null>(null)

  const createPearl = useCallback(
    async(newPearl:Pearl) => {
      try{
        const res  = await api.post('/pearl/create/', newPearl)
        if (Array.isArray(res)) {
          setData(res.data)
          return res.data
        }
        if (Array.isArray(res.data.results)) {
          setData(res.data.results)
          return res.data
        }
        return res
      } catch(err: any) {
        const message = err.response?.data?.detail || err.message || "Pearl was not created"
        setError(message)
        throw err
      }
    
  }, [])

  return {
    data,
    error,
    createPearl
  }
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

export function useTags(){
  return useQuery({
    queryKey: ['tags'],
    queryFn: async() => {
      const {data} = await api.get('/tags/')
      if (Array.isArray(data)){
        return data as Tag[]
      }
      if (data && Array.isArray(data.results)){
        return data.results as Tag[]
      }
      return [] as Tag[]
    }
  })
}

export function useFolders(){
  return useQuery({
    queryKey: ['folder'],
    queryFn: async() => {
      const {data} = await api.get('/folder/list')
      if (Array.isArray(data)){
        return data as Folder[]
      }
      if (data && Array.isArray(data.results)){
        return data.results as Folder[]
      }
      return [] as Folder[]
    }
  })
}

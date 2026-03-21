'use client'

import { Pearl, useFolders, usePearlActions, useTags } from "@/lib/hooks/usePearls";
import { useRouter } from "next/navigation";
import React, { useState } from "react";

export default function PearlCreateForm() {
  const router = useRouter()
  const { data: tags } = useTags()
  const { data: folders } = useFolders()
  const { createPearl } = usePearlActions()
  const [err, setErr] = useState<string | null>(null)
  const [formData, setFormData] = useState<Pearl>({
    id: "",
    title: '',
    content: '',
    content_type: '',
    url: '',
    is_public: true,
    created_at: '',
    updated_at: '',
    pearl_image: '',
    pearl_audio: '',
    pearl_video: '',
    pearl_category: '',
    pearl_summary: ''
  })

  const handleInputChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value, type } = e.target
    if (type === 'radio') {
      const checked = (e.target as HTMLInputElement).checked
      setFormData((prev) => ({ ...prev, [name]: checked }))
      return
    }
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const createPayload = <T extends Record<string, any>> (
    data:T, 
    optionalKeys: Array<keyof T>): Partial<T> => {
    return Object.fromEntries(
      Object.entries(data).filter(([key, value]) => {
        const isOptional = optionalKeys.includes(key as keyof T)
        if (!isOptional) return true
        if (value === undefined || value === null) return false
        if (typeof value === 'string' && value.trim() === '') return false
        return true
      })
    )
  }

  const handlePearlCreate = async (e: React.FormEvent) => {
    e.preventDefault()
    setErr(null)
    try {
      const payload = createPayload(formData, [
        'content_type', 
        'url', 
        'is_public',
        'created_at',
        'updated_at',
        'pearl_image',
        'pearl_audio',
        'pearl_category',
        'pearl_summary',
        'pearl_video'
      ])
      await createPearl(payload as Pearl)
      router.push('/pearls')
    } catch (err: any) {
      const message = err?.response?.data?.detail || err?.message || 'Pearl was not created'
      setErr(message)
      console.log(err)
    }
  }

  return (
    <div>
      <form onSubmit={handlePearlCreate}>
        <div className="text-2xl">Let's Write</div>
        <div>
          <label htmlFor="title"> Name this pearl</label>
          <input
            type="text"
            placeholder="Title"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="content"> Something more about it?</label>
          <input
            type="text"
            placeholder="What"
            id="content"
            name="content"
            value={formData.content || ''}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="content_type"> Content Type</label>
          <select
            id="content_type"
            name="content_type"
            value={formData.content_type || ''}
            onChange={handleInputChange}
          >
            <option value="">Select...</option>
            <option value="option_1">Option 1</option>
            <option value="option_2">Option 2</option>
            <option value="new_type">Add new type</option>
          </select>
        </div>
        <div>
          <label htmlFor="url"> Attache a link</label>
          <input
            type="text"
            placeholder="Title"
            id="url"
            name="url"
            value={formData.url || ''}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="tags"> Attach a Tag</label>
          <select id="tags">
            <option>
              Create New Tag
            </option>
            {tags?.map((tag) => (
              <option key={tag.id}>
                {tag.name}
              </option>
            ))}
          </select>
          <input type="text" placeholder="Create New Tag" />
        </div>
        <div>
          <label htmlFor="folder"> Add to Folder</label>
          <select id="folder">
            {folders?.map((folder) => (
              <option key={folder.id}>
                {folder.name}
              </option>
            ))}
            <option>Option 1</option>
            <option>Option 2</option>
            <option>Create new folder</option>
          </select>
        </div>
        <div>
          <label htmlFor="is_public"> Public</label>
          <input
            type="radio"
            id="is_public"
            name="is_public"
            checked={!!formData.is_public}
            onChange={handleInputChange}
          />
        </div>
        {err && <p className="text-red-600">{err}</p>}
        <div>
          <button type="submit">Save</button>
        </div>
      </form>
    </div>
  )
}

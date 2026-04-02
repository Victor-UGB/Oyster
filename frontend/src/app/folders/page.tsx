'use client'

import { ProtectedRoute } from "@/components/ProtectedRoute"
import { useFolders } from "@/lib/hooks/usePearls"

export default function FoldersPage(){
    const {data: folders, isLoading, error} = useFolders()
    return(
        <ProtectedRoute>
        <div>
            Folders
            <div>
                {folders?.map((folder, i) => (
                    <div key={i}>
                        <div>
                            {folder.name}
                        </div>
                    </div>
                ))}
            </div>
        </div>
        </ProtectedRoute>
    )
}
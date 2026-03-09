'use client'

import { ProtectedRoute } from "@/components/ProtectedRoute";
import { usePearlDetail, usePearls } from "@/lib/hooks/usePearls";
import { useParams } from "next/navigation";
import { useRouter } from "next/router";

export default function PearlDetailPage() {
    // const route = useRouter()
    const {id} = useParams()
    const response = usePearlDetail(id)
    const pearl = response.data
    return (
        <ProtectedRoute>
            <div>
                Pearl Page
                <div>
                    {pearl?.title}
                </div>
            </div>
        </ProtectedRoute>
    )
}
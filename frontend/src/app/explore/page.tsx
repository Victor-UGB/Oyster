'use client'

import { ProtectedRoute } from "@/components/ProtectedRoute";
import { usePearls } from "@/lib/hooks/usePearls";

export default function ExplorePage(){
    const {data: pearls, isLoading, error} = usePearls()

    return (
        <ProtectedRoute>
            <div>
                Explore Page
                <div>
                    {pearls?.map((pearl, i) => (
                        <div key={i}>
                            {pearl.content}
                        </div>
                    ))}
                </div>
            </div>
        </ProtectedRoute>
    )
}
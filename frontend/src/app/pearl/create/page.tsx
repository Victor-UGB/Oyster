'use client'

import PearlCreateForm from "@/components/PearlCreateForm";
import { ProtectedRoute } from "@/components/ProtectedRoute";


export default function PearlCreatePage(){
    return (
        <ProtectedRoute>
            Form
            <PearlCreateForm/>
        </ProtectedRoute>
    )
}
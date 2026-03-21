
import PearlCreateForm from "@/components/PearlCreateForm";
import { ProtectedRoute } from "@/components/ProtectedRoute";


export default async function PearlCreatePage(){
    return (
        <ProtectedRoute>
            Form
            <PearlCreateForm/>
        </ProtectedRoute>
    )
}
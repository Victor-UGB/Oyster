'use client'

import { useAuth } from "@/lib/hooks/useAuth";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function NavBar(){
    const {logout} = useAuth()
    const router = useRouter()
    const handleLogout = async () => {
        // Call logout funtion to unmount token
        await logout()
        // Push to login page after logout
        router.push("/login")
    }
    return(
        <div className="flex justify-evenly w-full">
            <div >
                ReMinded
            </div>
            <div>
                Menu
            </div>
            <Link href={"/pearl/create/"}>
            <div>
                Add pearl
            </div>
            </Link>
            <div>
                Search
            </div>
            <button onClick={handleLogout}>
                Log Out
            </button>
        </div>
    )
}

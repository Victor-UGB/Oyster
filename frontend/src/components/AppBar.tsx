import Link from "next/link"

export default function AppBar(){
    return(
        <div className="flex justify-evenly w-full">
            <div>
                Home
            </div>
            
            <div >
                Add Pearl
            </div>
            
            <div>
                Folders
            </div>
            <div>
                Explore
            </div>
        </div>
    )
}
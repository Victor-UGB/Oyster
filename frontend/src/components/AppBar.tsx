import Link from "next/link"

export default function AppBar(){
    return(
        <div className="flex justify-evenly w-full">
            <Link href={"/pearls/"}>
            <div>
                Home
            </div>
            </Link>
            <Link href={"/folders"}>
            <div >
                Folders
            </div>
            </Link>
            <Link href={"/explore"}>
            <div>
                Explore
            </div>
            </Link>
        </div>
    )
}
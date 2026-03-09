import Link from "next/link";

export default function NavBar(){
    return(
        <div className="flex justify-evenly w-full">
            <div >
                ReMinded
            </div>
            <div>
                Menu
            </div>
            <Link href={"/pearl/create"}>
            <div>
                Add pearl
            </div>
            </Link>
            <div>
                Search
            </div>
        </div>
    )
}

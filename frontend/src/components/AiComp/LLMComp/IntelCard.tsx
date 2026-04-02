import Link from "next/link";

export default function IntelCard(){
    return (
        <div>
            <Link
                          key={""}
                          href={`/pearl/${""}`}
                          className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 cursor-pointer"
                        >
                          <div className="mb-4">
                            <span className="inline-block px-3 py-1 text-xs font-semibold text-blue-700 bg-blue-100 rounded-full">
                              {"Intel"}
                            </span>
                          </div>
            
                          <h2 className="text-xl font-bold text-gray-800 mb-2 line-clamp-2">
                            {'Your Intel'}
                          </h2>
            
                          <p className="text-gray-600 text-sm mb-4 line-clamp-3">
                            {'No content'}
                          </p>
            
                          <div className="flex items-center justify-between text-xs text-gray-500">
                            {/* <span>{new Date(pearl.created_at).toLocaleDateString()}</span> */}
                            <span className={'text-green-600'}>
                              {'🔒 Private'}
                              ReMinded
                            </span>
                          </div>
                        </Link>
        </div>
    )
}
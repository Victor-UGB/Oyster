'use client'

import React, { useState } from "react"

export function UrlAiInput(){
    const [validURL, setValidURL] = useState<boolean>(false)
    const [value, setValue] = useState("")
    const [error, setError] = useState<string | null | undefined>("")
    const [touched, setTouched]  =  useState(false)
    const ALLOWED_DOMAINS = [
        "youtube.com",
        "instagram.com",
        "x.com",
        "twitter.com",
        "tiktok.com",
        "pinterest.com"
    ]

    const validateInput = (input:string) => {
        
        if (!input) return ""
        try {
            const url = new URL(input)
            if (!["http:", "https:"].includes(url.protocol)){
                return "Invalid protocol"
            }

            const hostname = url.hostname.toLowerCase();
            const isAllowed  = ALLOWED_DOMAINS.some(domain => hostname === domain || hostname.endsWith('.' + domain))
            console.log(`This is the url ${url}`)
            console.log(`This is the hostname ${hostname}`)
            console.log(isAllowed)
            if (!isAllowed){
                return "Only social media links can added"
            }
            return ""; // valid
        }catch (err){
            return "Invalid URL format"
        }

    }

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const {name, value} = e.target
        setTouched(true)

        const validationError = validateInput(value);
        setError(validationError)

    }
    return(
        <div className="w-full flex relative bottom-4 self-end">
            <div>
                {error? 
                <div>
                    {error}
                </div>: ""}
                
            <div className="w-full flex flex-col"> 
                <label htmlFor="url_input">Paste Url</label>           
                <input 
                id = "url_input"
                name="url_input"
            
                onChange={handleChange} 
                placeholder="Paste Url here"

                />
            </div>
            <div className="">
                <button disabled>Send</button>
            </div>
            </div>
        </div>
    )
}
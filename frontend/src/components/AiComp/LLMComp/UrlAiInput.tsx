'use client'

import { usePearlAnalyzer } from "@/lib/hooks/useOysterAi"
import React, { useState } from "react"
import AiPearlCreateForm from "./aiCreatePearlFromURLmodal"

export function UrlAiInput(){
    const [validURL, setValidURL] = useState<URL | undefined>()
    const [submittedURL, setsubmittedURL] = useState<URL | undefined>()
    const [value, setValue] = useState("")
    const [error, setError] = useState<string | null | undefined>("")
    const [touched, setTouched]  =  useState(false)
    const [aiCreatePearlForm, setAiCreatePearlForm] = useState(false)
    const [analysis, setAnalysis] = useState("")
    const ALLOWED_DOMAINS = [
        "youtube.com",
        "instagram.com",
        "x.com",
        "twitter.com",
        "tiktok.com",
        "pinterest.com"
    ]
    const analysisResult = usePearlAnalyzer(submittedURL)
    const urlAnalysis = async () => {
        try{
        
        setAnalysis(i => i = analysisResult)
        setAiCreatePearlForm(true)
        }
        catch(err){
            setAnalysis("Error in analysing url")
        }

    }

    const validateInput = (input:string) => {
        
        if (!input) return ""
        try {
            const normalized = /^https?:\/\//i.test(input) ? input : `https://${input}`
            const url = new URL(normalized)

            console.log("running check")
            if (!["http:", "https:"].includes(url.protocol)){
                return "Invalid protocol"
            }

            const hostname = url.hostname.toLowerCase();
            const isAllowed  = ALLOWED_DOMAINS.some(domain => hostname === domain || hostname.endsWith('.' + domain))
            console.log(`This is the url ${url}`)
            console.log(`This is the hostname ${hostname}`)
            console.log(isAllowed)
            if (!isAllowed){
                return "Only social media links can be added"
            }
            setValidURL(url)
            console.log(validURL)
            return "Valid Url"; // valid
        }catch (err){
            return "Invalid URL format"
        }

    }

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const {name, value} = e.target
        setTouched(true)
        // console.log(value)
        const validationError = validateInput(value);
        setError(validationError)
        if (validationError !== "Valid Url") {
            setValidURL(undefined)
            setsubmittedURL(undefined)
        }

    }

    const analyzeUrl = (url:URL | undefined) =>{
        console.log("analyzing url...")
        if(!validURL) return
        setsubmittedURL(validURL)
        urlAnalysis()
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
                <button
                onClick={() => analyzeUrl(validURL)}
                disabled={error === "Valid Url" ? false : true}
                className="disabled:bg-red-100 bg-blue-200"
                >
                    Save
                </button>
            </div>
            {submittedURL?
                <div>{analysis}</div>
                :""
            }
            </div>
            {aiCreatePearlForm? 
            <div className="absolute">
                <AiPearlCreateForm/>
            </div>: ""
            }
        </div>
    )
}

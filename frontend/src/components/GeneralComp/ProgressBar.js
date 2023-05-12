import React, { useState, useEffect } from "react";

export default function ProgressBar(props){
    const [progress, setProgress] = useState(0)

    const onScroll = () => {
        const winScroll = document.documentElement.scrollTop
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight
        const scrolled = (winScroll / height) * 100

        console.log(winScroll, height, scrolled)

        setProgress(scrolled)
    }

    useEffect(() => {
        window.addEventListener("scroll", onScroll)
    
        return () => {
        window.removeEventListener("scroll", onscroll)
        }
    }, [])
    

    return(
            <div className="progress-wrapper">
                <div className="progress-bar" style={{width: `${progress}%`}}></div>
            </div>
            
    )
} 
import React, {Component, useState, useEffect} from "react";
import {render} from "react-dom";

// import "./landingpage.css"

// const colors = ['green', 'red', 'yellow', 'purple', 'black']

export default function Hero(props){
    const colors = ['black', 'red', 'orange', 'purple', 'green']
    const [count, setCount] = useState(0)

    const [bgcolor, setbgColor] = useState(colors[count])

    function transitColor(){
        if(count < 4){
            setCount(count+1)
        }else{
            setCount(0)
        }
        setbgColor(colors[count])
    }
    // useEffect(() => {
        setInterval(() => {
                transitColor()
            }
        , 2000)
        
    // }) 

    return(
        <div className="light full-screen" style={{ backgroundColor: bgcolor, color: "white", transition: "ease-in-out 2s" }}>
            <div className="centralize-ys" >
                <div className="centralize-y">
                    <h1 className="font-h1">ONLY THE MOST BEAUTIFUL THINGS</h1>
                    <p className="font-h5">Share with the world the beauty of your world</p>
                </div>
                <div>
                    <div className="">
                        <form className="form1">
                            <input className="input1" type={"text"} placeholder={"Type in anything"}/>
                            <input className="input2" type={"submit"} value="Search"/>
                        </form>
                    </div>
                    <div>
                        <img />
                    </div>
                </div>
            </div>
        </div>
    )
}
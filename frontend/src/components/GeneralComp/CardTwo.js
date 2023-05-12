import React, { useState } from "react";
import Card from "./Card";
import Typewriter from "typewriter-effect"


export default function CardTwo(props){
    const articles = [
        {
            "id": 0, 
            "title": "Now the world can hear from you", 
            "subTitle": "Share Your Best", 
            "imgSoure": "https://images.unsplash.com/photo-1601972605341-b039a4f3ada7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8YXBwJTIwZmVhdHVyZXN8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60", 
            "para": "You can share thoughts and ideas and see how people benefit from them."
        },
        {
            "id": 1, 
            "title": "Share your ideas in text, sound and video", 
            "subTitle": "The Full Experience!", 
            "imgSoure": "https://images.unsplash.com/photo-1520333789090-1afc82db536a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80", 
            "para": "Give your viewers the full experience with the text, audio and video vblogs"
        },
    ]
    // const [selected, setSelected] = useState[articles[0]]
    return(
        <div style={{backgroundColor:"black", color: "white", transition: "ease-in-out 2s"}}>
            <div className='card-container'>
                <div>
                    <div className='section-title card-two-text'> {props.subTitle}</div>
                </div>
                <div>
                    <div className='font-h2 card-two-text'>{props.title}</div>
                </div>
                
                <div>
                    <div className="font-p3 card-two-text">
                    <Typewriter 
                                onInit={(typewiter) => {
                                    typewiter
                                        .typeString(props.para)
                                        // .pauseFor(2000)
                                        // .deleteAll()
                                        // .typeString("Do You")
                                        // .pauseFor(1000)
                                        // .deleteAll()
                                        // .typeString("Show Love")
                                        // .pauseFor(1000)
                                        // .deleteAll()
                                        // .typeString("Change Lives!")
                                        .start()
                                } 
                                }
                    />
                    </div>
                    {/* <div className='font-p3 card-two-text'>{props.para}</div> */}
                </div>
                {/* <div style={{padding: ".5rem 0rem 1rem 0rem"}}>
                    <Button 
                        name={props.actionBtn}
                        link={props.link}
                        btnClass= {props.btnClass}
                    />
                </div> */}
            </div>
            <hr style={{width: "70%", margin: "auto", border: ".5px  solid dimgray"}}/>
            <div style={{display: "flex", flexDirection: "row", overflow: "clip", overflowX: "scroll"}}>
                
                    {articles.map((article) => 
                        (<div className="card-two-card">
                            <Card
                            // subTitle = {article.subTitle}
                            title = {article.title}
                            imgSource = {article.imgSoure}
                            para = {article.para}
                            actionBtn = "See more"
                            btnClass = "action-button"
                            link = "/"
                            />
                        </div>))
                    }
            </div>
        </div>
    )
}
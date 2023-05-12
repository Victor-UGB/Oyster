import React, {Component} from "react";
import {BrowserRouter, Route, Routes, Link} from "react-router-dom";
import {render} from "react-dom";
import Hero from "./LandingPageComp/Hero";
import Navigation from "./GeneralComp/Navigation";
import Login from "./LoginComp/Login";
import Card from "./GeneralComp/Card";
import CardTwo from "./GeneralComp/CardTwo";
import Typewriter from "typewriter-effect"
import ProgressBar from "./GeneralComp/ProgressBar";
import Signup from "./SignupComp/Signup";

export default class LandingPage extends Component{
    constructor(props){
        super(props)
        this.state={
            count: 0,
            color: ['black', 'red', 'orange', 'purple', 'green']
        }
        this.transitColor = this.transitColor.bind(this)
    }

    transitColor(){
        if(this.state.count < 4){
            this.setState({count: this.state.count+1})
        }else{
            this.setState({count: 0})
        }
        this.setState({ color: this.state.color[count]})
    }
    // useEffect(() => {
    componentDidMount(){
        setInterval(() => {
            this.transitColor()
        }
        , 2000)
    }
    

    renderLandingPage(){
        return(
            <div className="light" style={{height: "100%"}}>
                {/* <div><Navigation/></div> */}
                <div><Hero/></div>
                <div>
                    <div>
                        <div className="section-title">
                            <Typewriter 
                                onInit={(typewiter) => {
                                    typewiter
                                        .typeString("The World is Your Community")
                                        .pauseFor(2000)
                                        .deleteAll()
                                        .typeString("Do You")
                                        .pauseFor(1000)
                                        .deleteAll()
                                        .typeString("Show Love")
                                        .pauseFor(1000)
                                        .deleteAll()
                                        .typeString("Change Lives!")
                                        .start()
                                } 
                                }
                            /> 
                        </div>
                        <div className="font-p3"> Share the beauty of your world to a boundless community, Let people around the world into your beautiful mind.</div>
                    </div>
                    <div>
                        <Card 
                            subTitle = "Share Your Best"
                            title = "Now the world can hear from you"
                            para = "You can share thoughts and ideas and see how people benefit from them."
                            actionBtn = "Try for free"
                            link="/login"
                            btnClass ="action-button"
                            imgSource="https://images.unsplash.com/photo-1544773088-d142e38f5793?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=813&q=80"
                        />
                        <Card 
                            subTitle = "The Full Experience!"
                            title = "Share your ideas in text, sound and video"
                            para = "Give your viewers the full experience with the text, audio and video vblogs"
                            actionBtn = "Try for free"
                            link = "/login"
                            btnClass = "action-button"
                            imgSource="https://images.unsplash.com/photo-1593733925160-6f78dc0be8b6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8aG9sZGluZyUyMHBob25lfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60"
                        />
                        <CardTwo
                            subTitle= "With Oyst"
                            title = ""
                            para = "Your creations are pearls. Be free to open up here."
                            colorSwitch = {this.state.color[this.state.count]}
                        />
                    </div>
                </div>
                With Oyst, your creations are pearls. Be free to open up here.
                
            </div>
        )
    }



    render(){
        return(
            <div>
                <div>
                    <BrowserRouter>
                        <ProgressBar/>
                        <Navigation/>
                        <Routes>
                            <Route>
                                <Route path="/" element={this.renderLandingPage()}/>
                                <Route path="/login" element={<Login/>}/>
                                <Route path="/signup" element={<Signup/>}/>
                            </Route>
                        </Routes>
                    </BrowserRouter>
                </div>
            </div>
        )
    }
}
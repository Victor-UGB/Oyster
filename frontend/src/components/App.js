import React, {Component} from "react";
import {render} from "react-dom";
import LandingPage from "./LandingPage";
import ProgressBar from "./GeneralComp/ProgressBar";

export default class App extends Component{
    constructor(props){
        super(props)

    }
    render(){
        return(
            <div>
            {/* <h1>Testing React Frontend</h1> */}
            
            <LandingPage/>
            </div>
        ) 
    }
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);
import React, {Component} from "react";

export default function Signup(props){
    return(
        <div className="auth-form-container">
            <div className="auth-form">
                <h1 className="font-h1" style={{padding: "0.5rem 2rem"}}>Oyster <br/>Sign Up</h1>
                <form className="login-form2">
                    <input className="input3" type="text" placeholder="Fullname"/>
                    <input className="input3" type="text" placeholder="Email"/>
                    <input className="input3" type="text" placeholder="Create Username"/>
                    <div><input className="input3" type="password" placeholder="Password"/></div>
                    <div><input className="input3" type="password" placeholder="Confirm Password"/></div>
                    <input className="login-button" type="submit" value="Sign Up"/>
                </form>
                {/* <div className="font-h5" style={{padding: "0.5rem 2rem"}}><a href="/">Forgotten Password?</a></div> */}
            </div>
        </div>
    )
}

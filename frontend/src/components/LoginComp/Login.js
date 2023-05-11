import React, {Component} from "react";

export default function Login(props){
    return(
        <div className="auth-form-container">
            <div className="auth-form">
                <h1 className="font-h1" style={{padding: "0.5rem 2rem"}}>Oyster <br/>Login</h1>
                <form className="login-form">
                    <input className="input1" type="text" placeholder="Username"/>
                    <input className="input1" type="password" placeholder="Password"/>
                    <input className="login-button" type="submit" value="Login"/>
                </form>
                <div className="font-h5" style={{padding: "0.5rem 2rem"}}><a href="/">Forgotten Password?</a></div>
            </div>
        </div>
    )
}

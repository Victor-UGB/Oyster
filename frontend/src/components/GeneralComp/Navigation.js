import React, {Component, useState} from "react"
import {BrowserRouter, Link, Route, Routes, useNavigate} from "react-router-dom"
import Login from "../LoginComp/Login"
import Button from "./Button";

// export default function Navigation(props){
//     const navigate =useNavigate()

//     return(
//         <div>
//             <div>
//                 <button>
//                     Login
//                 </button>
//                 {/* <Link>
//                 <button>Login</button>
//                 </Link>
//                 <Link>
//                 <button>Sign Up</button>
//                 </Link>
//                 <Link>
//                 <button>Commitments</button>
//                 </Link> */}
//             </div>
//             <div>
//                 Navigation
//                 <Login/>
//             </div>
//         </div>
//     )
// }

export default class Navigation extends Component{
    constructor(props){
        super(props);
        this.state ={
            openMenu : false,
            navItems : [
                {'id': 1, 'name': 'Home', 'link': '/', 'btnClass': 'nav-button'},
                {'id': 2, 'name': 'Login', 'link': '/login', 'btnClass': 'nav-button'},
                {'id': 3, 'name': 'Sign Up', 'link': '/signup', 'btnClass': 'nav-button'}
            ]
        }
        // this.openMenu = this.openMenu.bind(this)
    }



    renderNav(){
        return(
            <div >
                <a href="/"><div className="brand">OYSTER</div></a>
                <div className="abs1">
                    <div> <button className="nav-button1" onClick={() => this.setState({openMenu : !this.state.openMenu})}>Menu</button></div>
                    <div className={this.state.openMenu == false? "hide-display": "show-display"}>
                        {/* <div>
                            <Link to="/">
                            <button onClick={() => setState({openMenu : false})} className="nav-button">Home</button>
                            </Link>
                        </div>
                        <div>
                            <Link to="/login">
                            <button className="nav-button">Login</button>
                            </Link>
                        </div>
                        <div className="nav-button">
                            <Button 
                                name={"Home"}
                                link={"/"}
                            />
                        </div> */}
                        {this.state.navItems.map((button) => 
                            (<div>
                                <Button 
                                name={button.name} 
                                link={button.link}
                                btnClass={button.btnClass}
                                />
                            </div>))
                        }
                    </div>
                </div>
            </div>
        )
    }

    render(){
        return(
            <div>
                <div>
                    {this.renderNav()}
                </div>
            </div>
        )
    }
}


import React from "react";
import { Link } from "react-router-dom";

export default function Button(props){
    return(
        <div>
            <Link to={props.link}>
            <button className={props.btnClass}>
                {props.name}
            </button>
            </Link>
        </div>
    )
}
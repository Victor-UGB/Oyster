import React from 'react';
import Button from './Button';

export default function Card(props){
    return(
        <div className='card-container'>
            <div>
                <div className='font-h7 card-subtitle'>{props.subTitle}</div>
            </div>
            <div>
                <div className='card-img-container'>
                    <img className='card-img' src={props.imgSource}/>
                </div>
            </div>
            <div>
                <div className='font-h2 card-title'>{props.title}</div>
            </div>
            
            <div>
                <div className='font-p2'>{props.para}</div>
            </div>
            <div style={{padding: ".5rem 0rem 1rem 0rem"}}>
                <Button 
                    name={props.actionBtn}
                    link={props.link}
                    btnClass= {props.btnClass}
                />
            </div>
        </div>
    )
}
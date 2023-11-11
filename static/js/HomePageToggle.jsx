import React from 'react';
import '../css/main.css';

export function HomePageToggle(){
    return(
        <div id='home-page-toggle-component'  className='full-height'>
        <div 
            className='toggle-container'>
            <div id='toggle-0'>
                Latest Projects
            </div>
        </div>
        </div>
    );
}
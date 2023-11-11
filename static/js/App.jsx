import React from 'react';
import '../css/main.css';
import { HomePageToggle } from './HomePageToggle.jsx';

export function App(){
    return(
        <div id='app-component' className='full-height'>
            <HomePageToggle/>
        </div>
    );
}
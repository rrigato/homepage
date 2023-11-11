import React from 'react';
import '../css/main.css';
import { HomePageToggle } from './HomePageToggle';

export function App(){
    return(
        <div id='app-entry-point'>
            <HomePageToggle/>
        </div>
    );
}
import React, { useState } from 'react';
import '../css/homepageSection.css';


/**Details about the website
 * 
 * @returns react jsx 
 */
export function About(){
    return(
        <div className='homepage-content'>
            <h3>What do I need to know about this website?</h3>
            <div>
                <ul>
                    <li>Anytime I look back at an application I built more than a year I am embarrased by the quality of the architecture. This is the trademark of a good engineer because it means they are always improving their kraft.</li>
                    <li>This webiste went from a Java EE2 web app hosted in google app engine all the way to serverless web app deployed to AWS...with many migration tears in between!</li>
                    <li>The world's largest tuned mass damper is at the 
                        <a href='https://en.wikipedia.org/wiki/Tuned_mass_damper'>Taipei 101</a>
                    </li>
                </ul>
            </div>
        </div>
    );
}
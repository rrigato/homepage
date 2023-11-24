import React, { useState } from 'react';
import '../css/homepageSection.css';


/**Details about the website
 * 
 * @returns react jsx 
 */
export function About(){
    return(
        <div className='homepage-content'>
            <div>
                <ul>
                    <h3>What do I need to know about this website?</h3>
                    <li>
                        <a href='https://github.com/rrigato/homepage'>source code </a>
                    </li>
                    <li>I strive to be embarrassed by the quality of the architecture of any application I have built that is more than a year old. </li>
                    <li>Strive to constantly be improving your craft.</li>
                    <li>How do you practice your skills in the same way a musician practices cords?</li>

                    <li>This webiste went from a Java EE2 web app hosted in google app engine 
                        all the way to serverless web app deployed to AWS</li>
                    <li>Run a <code>git log --before="2018-01-01"</code> on the source code for a stroll down memory lane!</li>
                    
                    <li>The world's largest tuned mass damper is at the 
                        <a href='https://en.wikipedia.org/wiki/Tuned_mass_damper'>Taipei 101</a>
                    </li>
                </ul>
            </div>
        </div>
    );
}
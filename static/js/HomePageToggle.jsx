import React, { useState } from 'react';
import '../css/main.css';


/**Toggle button for different sections of homepage
 * 
 * @returns react jsx 
 */
export function HomePageToggle(){
    /**
     * @type {[Number, Function]}
     */
    const [selectedSection, setSelectedSelection] = useState(0);
    return(
        <div id='home-page-toggle-component'  className='full-height'>
            <div className='toggle-container'>
                <div id='button-container' className='flex-container'>
                    <div className='toggle-button-container'>
                        <button
                            className={
                                selectedSection === 0 ?
                                'toggle-button toggle-currently-selected-button':
                                'toggle-button'
                            }
                            onClick={
                                (buttonEvent) => {
                                    buttonEvent.preventDefault();
                                    setSelectedSelection(0);
                                }
                            }
                        
                        >
                        Projects
                        </button>
                    </div>
                    
                    <div className='toggle-button-container'>
                        <button
                            className={
                                selectedSection === 1 ?
                                'toggle-button toggle-currently-selected-button':
                                'toggle-button'
                            }
                            onClick={
                                (buttonEvent) => {
                                    buttonEvent.preventDefault();
                                    setSelectedSelection(1);
                                }
                            }
                        >
                        About
                        </button>
                    </div>
                    
                    <div className='toggle-button-container'>
                        <button
                            className={
                                selectedSection === 2 ?  
                                'toggle-button toggle-currently-selected-button':
                                'toggle-button'
                            }
                            onClick={
                                (buttonEvent) => {
                                    buttonEvent.preventDefault();
                                    setSelectedSelection(2);
                                }
                            }
                        >
                        Book Recommendations
                        </button>
                    </div>
                </div>
                <div 
                    id='toggle-0' 
                    
                    hidden= {
                        selectedSection !== 0
                    }>
                    <div className='homepage-content'>
                        <ul>
                            <h3>Amazon Alexa Skill To retrieve Television Ratings</h3>
                            <li>Provides television ratings for the Adult Swim Saturday night Toonami television block.</li>
                            <li><a href='https://www.amazon.com/dp/B0B5596H7C/'>Application link</a></li>
                            <li><a href='https://github.com/rrigato/tvratings'>Source Code</a></li>

                            <h3>Amazon Alexa Air Quality Burning Restriction Skill</h3>
                            <li>Amazon Alexa skill to determine if a zip code has any fuel burning restrictions for heating your home in the winter.</li>
                            <li><a href='https://www.amazon.com/dp/B09PVD9VSC/'>Application link</a></li>
                            <li><a href='https://github.com/rrigato/burnday'>Source Code</a></li>

                            <h3>Web scrap television network ratings</h3>
                            <li>Only location on the internet that has an archive of Adult Swim Toonami Ratings in a programmable format.</li>
                            <li>Reach out to me on github if you would like access.</li>
                            <li><sup><sup>First rule of building a sustainable web scraping application is to never build a web scrapping application.</sup></sup></li>
                            <li><a href='https://github.com/rrigato/ratings'>Source Code</a></li>

                            <h3>Github 3d commit history webpage</h3>
                            <li>Automates creation of 3D commit history to populate web application artifacts</li>
                            <li><a href='https://github.com/rrigato/rrigato/blob/master/README.md'>Application link</a></li>
                            <li><a href='https://github.com/rrigato/rrigato/'>Source Code</a></li>
                        </ul>

                    </div>
                </div>
                <div 
                    id='toggle-1' 
                    
                    hidden= {
                        selectedSection !== 1
                    }>
                    About me
                </div>
                <div 
                    id='toggle-2' 
                    
                    hidden= {
                        selectedSection !== 2
                    }>
                    Latest Books
                </div>
            </div>
        </div>
    );
}
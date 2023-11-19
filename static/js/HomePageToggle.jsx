import React, { useState } from 'react';
import '../css/main.css';
import { Projects } from './Projects.jsx';


/**Toggle button for different sections of homepage
 * 
 * @returns react jsx 
 */
export function HomePageToggle(){
    /**Section of the webpage the user wants to view
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
                {
                    selectedSection === 0 ? <Projects/> :
                    <div hidden={true}></div>
                }
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
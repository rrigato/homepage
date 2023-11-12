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
                            autoFocus={selectedSection === 0}
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
                            autoFocus={selectedSection === 1}
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
                            autoFocus={selectedSection === 2}
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
                        Blog
                        </button>
                    </div>
                </div>
                <div 
                    id='toggle-0' 
                    
                    hidden= {
                        selectedSection !== 0
                    }>
                    Latest Projects
                </div>
            </div>
        </div>
    );
}
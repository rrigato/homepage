import React, { useState } from 'react';
import '../css/main.css';

export function HomePageToggle(){
    /**
     * @type {[Number, Function]}
     */
    const [selectedSection, setSelectedSelection] = useState(0);
    return(
        <div id='home-page-toggle-component'  className='full-height'>
            <div className='toggle-container'>
                <div id='button-container'>
                    <button
                        className='toggle-button'
                        onClick={
                            () => {
                                setSelectedSelection(0);
                            }
                        }
                    >
                    Projects
                    </button>
                    
                    <button
                        className='toggle-button'
                        onClick={
                            () => {
                                setSelectedSelection(1)
                            }
                        }
                    >
                    About
                    </button>
                    
                    <button
                        className='toggle-button'
                        onClick={
                            () => {
                                setSelectedSelection(2)
                            }
                        }
                    >
                    Blog
                    </button>
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
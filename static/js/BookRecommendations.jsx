import React from 'react';
import '../css/homepageSection.css';

/**Book Recommendations
 * 
 * @returns react jsx 
 */
export function BookRecommendations(){
    return(
        <div className='homepage-content'>
            <div>
                <ul>
                    <h3>Everyday Reads</h3>
                    <h3>Software Engineering</h3>
                </ul>
            </div>
        </div>
    );
}
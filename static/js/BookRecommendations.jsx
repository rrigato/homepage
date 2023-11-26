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
                    <li>Incerto by
                        <a href='https://en.wikipedia.org/wiki/Nassim_Nicholas_Taleb#Writing_career'>Nassim Taleb</a>
                        <li className='book-details'>
                            Five book collection centered around the understanding of randomness in your everyday life.
                            
                        </li>

                    </li>

                    <h3>Software Engineering</h3>
                </ul>
            </div>
        </div>
    );
}
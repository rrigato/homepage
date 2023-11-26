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

                    </li>
                    <li className='book-details'>
                        Five book collection centered around the understanding of randomness in your everyday life.
                        
                    </li>


                    <h3>Software Engineering</h3>
                    
                    <li>Clean Architecture by
                        <a href='https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164'>Bob Martin</a>
                    </li>
                    <li className='book-details'>
                        The goal of software architecture is to minimize the human resources required to build and maintain the desired application.
                    </li>

                    <li>Rework by
                        <a href='https://basecamp.com/books/rework'
                        >DHH and Jason Fried</a>
                    </li>
                    <li className='book-details'>
                        Outlines office culture for working remote
                    </li>
                    
                    <li>Shape Up by
                        <a href='https://basecamp.com/shapeup'>Ryan Singer</a>
                    </li>
                    <li className='book-details'>
                        Outside of the fact that he objectively has the coolest first name a human can have,
                        this is the definitive guide on how iterations should be structured in any devops oriented team.
                    </li>

                </ul>
            </div>
        </div>
    );
}
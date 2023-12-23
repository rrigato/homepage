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
                        <a 
                            href='https://en.wikipedia.org/wiki/Nassim_Nicholas_Taleb#Writing_career'
                            target={'_blank'}
                        >Nassim Taleb</a>

                    </li>
                    <li className='book-details'>
                        Five book collection centered around the understanding the impacts of randomness.
                    </li>

                    <li>Outlive by
                        <a 
                            href='https://www.amazon.com/Outlive-Longevity-Peter-Attia-MD/dp/0593236599'                        
                            target={'_blank'}
                        >Peter Attia</a>

                    </li>
                    <li className='book-details'>
                        View health span as a constant downward slope instead of a constant as years pass by.
                    </li>

                    <li>The Life Cleaning Magic Of Tidying Up by
                        <a 
                            href='https://www.amazon.com/Life-Changing-Magic-Tidying-Decluttering-Organizing/dp/1607747308'                        
                            target={'_blank'}
                        >Marie Kondo</a>

                    </li>
                    <li className='book-details'>
                        Evaluate each item in your life for whether it continues to bring you joy.
                    </li>

                    <li>The Power Of Bad by
                        <a 
                            href='https://www.amazon.com/Power-Bad-Negativity-Effect-Rules-ebook/dp/B07Q3NHPGZ'                        
                            target={'_blank'}
                        > John Tierney and Roy Baumeister</a>

                    </li>
                    <li className='book-details'>
                        Having 1 friend with a negative personality is asymmetrically harmful to your well being.
                    </li>


                    <h3>Software Engineering</h3>

                    <li>Clean Architecture by
                        <a 
                            href='https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164'
                            target={'_blank'}
                        >Bob Martin</a>
                    </li>
                    <li className='book-details'>
                        The goal of software architecture is to minimize the human resources required to build and maintain the desired application.
                    </li>

                    <li>Rework by
                        <a 
                            href='https://basecamp.com/books/rework'                        
                            target={'_blank'}
                        >DHH and Jason Fried</a>
                    </li>
                    <li className='book-details'>
                        Outlines office culture for working remote
                    </li>

                    <li>Shape Up by
                        <a 
                            href='https://basecamp.com/shapeup'
                            target={'_blank'}
                        >Ryan Singer</a>
                    </li>
                    <li className='book-details'>
                        Outside of the fact that he objectively has the coolest first name a human can have,
                        this is the definitive guide on how iterations should be structured in any devops oriented team.
                    </li>

                    <li>The Mythical Man Month by
                        <a 
                            href='https://en.wikipedia.org/wiki/The_Mythical_Man-Month'                        
                            target={'_blank'}
                        >Fred Brooks</a>
                    </li>
                    <li className='book-details'>
                        Scaling software engineering team size leads to increased communication overhead 
                        and might cause the project miss deadlines.
                    </li>

                </ul>
            </div>
        </div>
    );
}
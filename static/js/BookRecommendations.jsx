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
                        Five book collection centered around the understanding the impacts of randomness.
                    </li>

                    <li>Outlive by
                        <a href='https://www.amazon.com/Life-Changing-Magic-Tidying-Decluttering-Organizing/dp/1607747308'
                        >Peter Attia</a>

                    </li>
                    <li className='book-details'>
                        View health span as a constant downward slope instead of constant as years pass by
                    </li>

                    <li>The Life cleaning magic of tidying up by
                        <a href='https://www.amazon.com/Life-Changing-Magic-Tidying-Decluttering-Organizing/dp/1607747308'
                        >Marie Kondo</a>

                    </li>
                    <li className='book-details'>
                        Remove any items in your life if they do not bring you joy.
                    </li>

                    <li>The power of bad by
                        <a href='https://www.amazon.com/Power-Bad-Negativity-Effect-Rules-ebook/dp/B07Q3NHPGZ'
                        > John Tierney and Roy Baumeister</a>

                    </li>
                    <li className='book-details'>
                        Having 1 friend with a negative personality is asymmetrically harmful to your well being.
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
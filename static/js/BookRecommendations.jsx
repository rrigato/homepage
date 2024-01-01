import React from 'react';
import '../css/homepageSection.css';

/**
 * @type {string[]} bookDescriptions summary of book
 */
const bookDescriptions = [
    'Five book collection centered around the understanding the impacts of randomness.',
    'View health span as a constant downward slope instead of a constant as years pass by.',
    'Evaluate each item in your life for whether it continues to bring you joy.',
    'Having 1 friend with a negative personality is asymmetrically harmful to your well being.',
    'The goal of software architecture is to minimize the human resources required to build and maintain the desired application.',
    'Outlines office culture for working remote',
    'Outside of the fact that he objectively has the coolest first name a human can have, this is the definitive guide on how iterations should be structured in any devops oriented team.',
    'Scaling software engineering team size leads to increased communication overhead and might cause the project to miss deadlines.'    
]

/**
 * @type {string[]} bookTitles list of book titles
 */
const bookTitles = [
    'Incerto by',
    'Outlive by',
    'The Life Cleaning Magic Of Tidying Up by',
    'The Power Of Bad by',
    'Clean Architecture by',
    'Rework by',
    'Shape Up by',
    'The Mythical Man Month by'
]

/**
 * @type {string[]} bookUrls list of book urls
 */
const bookUrls = [
    'https://en.wikipedia.org/wiki/Nassim_Nicholas_Taleb#Writing_career',
    'https://www.amazon.com/Outlive-Longevity-Peter-Attia-MD/dp/0593236599',
    'https://www.amazon.com/Life-Changing-Magic-Tidying-Decluttering-Organizing/dp/1607747308',
    'https://www.amazon.com/Power-Bad-Negativity-Effect-Rules-ebook/dp/B07Q3NHPGZ',
    'https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164',
    'https://basecamp.com/books/rework',
    'https://basecamp.com/shapeup',
    'https://en.wikipedia.org/wiki/The_Mythical_Man-Month'

]
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
                    <li>{bookTitles[0]}
                        <a 
                            href={bookUrls[0]}
                            target={'_blank'}
                        >Nassim Taleb</a>

                    </li>
                    <li className='book-details'>
                        {bookDescriptions[0]}
                    </li>

                    <li>{bookTitles[1]}
                        <a 
                            href={bookUrls[1]}
                            target={'_blank'}
                        >Peter Attia</a>

                    </li>
                    <li className='book-details'>
                        {bookDescriptions[1]}
                    </li>

                    <li>{bookTitles[2]}
                        <a 
                            href={bookUrls[2]}
                            target={'_blank'}
                        >Marie Kondo</a>

                    </li>
                    <li className='book-details'>
                        {bookDescriptions[2]}
                    </li>

                    <li>{bookTitles[3]}
                        <a 
                            href={bookUrls[3]}
                            target={'_blank'}
                        > John Tierney and Roy Baumeister</a>

                    </li>
                    <li className='book-details'>
                        {bookDescriptions[3]}
                    </li>


                    <h3>Software Engineering</h3>

                    <li>{bookTitles[4]}
                        <a 
                            href={bookUrls[4]}
                            target={'_blank'}
                        >Bob Martin</a>
                    </li>
                    <li className='book-details'>
                        {bookDescriptions[4]}
                    </li>

                    <li>{bookTitles[5]}
                        <a 
                            href={bookUrls[5]}
                            target={'_blank'}
                        >DHH and Jason Fried</a>
                    </li>
                    <li className='book-details'>
                        {bookDescriptions[5]}
                    </li>

                    <li>{bookTitles[6]}
                        <a 
                            href={bookUrls[6]}
                            target={'_blank'}
                        >Ryan Singer</a>
                    </li>
                    <li className='book-details'>
                        {bookDescriptions[6]}
                    </li>

                    <li>{bookTitles[7]}
                        <a 
                            href={bookUrls[7]}
                            target={'_blank'}
                        >Fred Brooks</a>
                    </li>
                    <li className='book-details'>
                        {bookDescriptions[7]}
                    </li>

                </ul>
            </div>
        </div>
    );
}
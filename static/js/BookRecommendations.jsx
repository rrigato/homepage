import React from 'react';
import '../css/homepageSection.css';


/**Books to recommend and meta data
 * 
 * @type {Array.<{
 *  bookAuthor: string, 
 *  bookDescription: string, 
 *  bookTitle: string, 
 *  bookUrl: string
 * }>} bookData
 */
const bookData = [
    {
        bookAuthor: 'Nassim Taleb',
        bookDescription: 'Five book collection centered around the understanding the impacts of randomness.',
        bookTitle: 'Incerto',
        bookUrl: 'https://en.wikipedia.org/wiki/Nassim_Nicholas_Taleb#Writing_career'
    },
    {
        bookAuthor: 'Peter Attia',
        bookDescription: 'View health span as a downward slope instead of a constant as the years pass by.',
        bookTitle: 'Outlive',
        bookUrl: 'https://www.amazon.com/Outlive-Longevity-Peter-Attia-MD/dp/0593236599'
    },
    {
        bookAuthor: 'Marie Kondo',
        bookDescription: 'Evaluate each item in your life for whether it continues to bring you joy.',
        bookTitle: 'The Life Changing Magic Of Tidying Up',
        bookUrl: 'https://www.amazon.com/Life-Changing-Magic-Tidying-Decluttering-Organizing/dp/1607747308'
    },
    {
        bookAuthor: 'John Tierney and Roy Baumeister',
        bookDescription: 'Having 1 friend with a negative personality is asymmetrically harmful to your well being.',
        bookTitle: 'The Power Of Bad',
        bookUrl: 'https://www.amazon.com/Power-Bad-Negativity-Effect-Rules-ebook/dp/B07Q3NHPGZ'
    },
    {
        bookAuthor: 'Bob Martin',
        bookDescription: 'The goal of software architecture is to minimize the human resources required to build and maintain the desired application.',
        bookTitle: 'Clean Architecture',
        bookUrl: 'https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164'
    },
    {
        bookAuthor: 'DHH and Jason Fried',
        bookDescription: 'Outlines office culture for working remote',
        bookTitle: 'Rework',
        bookUrl: 'https://basecamp.com/books/rework'
    },
    {
        bookAuthor: 'Ryan Singer',
        bookDescription: 'Outside of the fact that he objectively has the coolest first name a human can have, this is the definitive guide on how iterations should be structured in any devops oriented team.',
        bookTitle: 'Shape Up',
        bookUrl: 'https://basecamp.com/shapeup'
    },
    
    {
        bookAuthor: 'Fred Brooks',
        bookDescription: 'Scaling software engineering team size leads to increased communication overhead and might cause the project to miss deadlines.',
        bookTitle: 'The Mythical Man Month by',
        bookUrl: 'https://en.wikipedia.org/wiki/The_Mythical_Man-Month'
        
    },
]

/**Book Recommendations
 *
 * @returns react jsx
 */
export function BookRecommendations(){
    /**
     * @type {Array.<JSX.Element>} bookJsxListItems list of li from bookData
     */ 
    const bookJsxListItems = [];
    
    //for loop over bookData array
    for(let i = 0; i < bookData.length; i++){
        bookJsxListItems.push(
            <div>
                <li>{bookData[i].bookTitle}
                    <a
                        href={bookData[i].bookUrl}
                        target={'_blank'}
                    >{bookData[i].bookAuthor}</a>
                </li>
                <li className='book-details'>
                    {bookData[i].bookDescription}
                </li>
            </div>
        );
    }
    return(
        <div className='homepage-content'>
            <div>
                <ul>
                    <h3>Everyday Reads</h3>
                    <li>{bookData[0].bookTitle}
                        <a 
                            href={bookData[0].bookUrl}
                            target={'_blank'}
                        >{bookData[0].bookAuthor}</a>

                    </li>
                    <li className='book-details'>
                        {bookData[0].bookDescription}
                    </li>

                    <li>{bookData[1].bookTitle}
                        <a 
                            href={bookData[1].bookUrl}
                            target={'_blank'}
                        >{bookData[1].bookAuthor}</a>

                    </li>
                    <li className='book-details'>
                        {bookData[1].bookDescription}
                    </li>

                    <li>{bookData[2].bookTitle}
                        <a 
                            href={bookData[2].bookUrl}
                            target={'_blank'}
                        >{bookData[2].bookAuthor}</a>

                    </li>
                    <li className='book-details'>
                        {bookData[2].bookDescription}
                    </li>

                    <li>{bookData[3].bookTitle}
                        <a 
                            href={bookData[3].bookUrl}
                            target={'_blank'}
                        >{bookData[3].bookAuthor}</a>

                    </li>
                    <li className='book-details'>
                        {bookData[3].bookDescription}
                    </li>


                    <h3>Software Engineering</h3>

                    <li>{bookData[4].bookTitle}
                        <a 
                            href={bookData[4].bookUrl}
                            target={'_blank'}
                        >{bookData[4].bookAuthor}</a>
                    </li>
                    <li className='book-details'>
                        {bookData[4].bookDescription}
                    </li>

                    <li>{bookData[5].bookTitle}
                        <a 
                            href={bookData[5].bookUrl}
                            target={'_blank'}
                        >{bookData[5].bookAuthor}</a>
                    </li>
                    <li className='book-details'>
                        {bookData[5].bookDescription}
                    </li>

                    <li>{bookData[6].bookTitle}
                        <a 
                            href={bookData[6].bookUrl}
                            target={'_blank'}
                        >{bookData[6].bookAuthor}</a>
                    </li>
                    <li className='book-details'>
                        {bookData[6].bookDescription}
                    </li>

                    <li>{bookData[7].bookTitle}
                        <a 
                            href={bookData[7].bookUrl}
                            target={'_blank'}
                        >{bookData[7].bookAuthor}</a>
                    </li>
                    <li className='book-details'>
                        {bookData[7].bookDescription}
                    </li>

                </ul>
            </div>
        </div>
    );
}
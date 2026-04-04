import React, { useState } from 'react';

const bookData = [
    {
        id: 1,
        title: 'Incerto',
        author: 'Nassim Taleb',
        description: 'Five book collection centered around the understanding the impacts of randomness.',
        url: 'https://en.wikipedia.org/wiki/Nassim_Nicholas_Taleb#Writing_career'
    },
    {
        id: 2,
        title: 'Outlive',
        author: 'Peter Attia',
        description: 'View health span as a downward slope instead of a constant as the years pass by.',
        url: 'https://www.amazon.com/Outlive-Longevity-Peter-Attia-MD/dp/0593236599'
    },
    {
        id: 3,
        title: 'The Life Changing Magic Of Tidying Up',
        author: 'Marie Kondo',
        description: 'Evaluate each item in your life for whether it continues to bring you joy.',
        url: 'https://www.amazon.com/Life-Changing-Magic-Tidying-Decluttering-Organizing/dp/1607747308'
    },
    {
        id: 4,
        title: 'The Power Of Bad',
        author: 'John Tierney and Roy Baumeister',
        description: 'Having 1 friend with a negative personality is asymmetrically harmful to your well being.',
        url: 'https://www.amazon.com/Power-Bad-Negativity-Effect-Rules-ebook/dp/B07Q3NHPGZ'
    },
    {
        id: 5,
        title: 'Clean Architecture',
        author: 'Bob Martin',
        description: 'The goal of software architecture is to minimize the human resources required to build and maintain the desired application.',
        url: 'https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164'
    },
    {
        id: 6,
        title: 'Rework',
        author: 'DHH and Jason Fried',
        description: 'Outlines office culture for working remote',
        url: 'https://basecamp.com/books/rework'
    },
    {
        id: 7,
        title: 'Shape Up',
        author: 'Ryan Singer',
        description: 'The definitive guide on how iterations should be structured in any devops oriented team.',
        url: 'https://basecamp.com/shapeup'
    },
    {
        id: 8,
        title: 'The Mythical Man Month',
        author: 'Fred Brooks',
        description: 'Scaling software engineering team size leads to increased communication overhead and might cause the project to miss deadlines.',
        url: 'https://en.wikipedia.org/wiki/The_Mythical_Man-Month'
    }
];

export function BookRecommendations() {
    const [activeBook, setActiveBook] = useState(0);

    const scrollToBook = (index) => {
        setActiveBook(index);
        const container = document.querySelector('.books-container');
        if (container) {
            const firstCard = container.querySelector('.book-card');
            const cardWidth = firstCard ? firstCard.getBoundingClientRect().width + 20 : 220;
            container.scrollTo({
                left: index * cardWidth,
                behavior: 'smooth'
            });
        }
    };

    return (
        <div>
            <div className="section-title">RECOMMENDATIONS</div>
            <h2 className="section-heading">Book Recommendations</h2>
            <p className="about-description">
                Books that have shaped the way I think about software, systems, and life.
            </p>

            <button className="cta-button" style={{ marginBottom: '60px' }}>
                BROWSE MY LIST
                <span>+</span>
            </button>

            <div className="books-carousel">
                <div className="books-container">
                    {bookData.map((book, index) => (
                        <a
                            key={book.id}
                            className="book-card"
                            href={book.url}
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            <div className="book-content">
                                <h4 className="book-title">{book.title}</h4>
                                <p className="book-author">{book.author}</p>
                                <p className="book-description">{book.description}</p>
                            </div>
                        </a>
                    ))}
                </div>

                <div className="carousel-pagination">
                    {bookData.map((_, index) => (
                        <button
                            key={index}
                            className={`pagination-dot ${activeBook === index ? 'active' : ''}`}
                            onClick={() => scrollToBook(index)}
                        >
                            {String(index + 1).padStart(2, '0')}
                        </button>
                    ))}
                </div>
            </div>
        </div>
    );
}

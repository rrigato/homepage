import React from 'react';

export function Header() {
    const scrollToSection = (sectionId) => {
        const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    return (
        <header className="header">
            <div className="logo">RR</div>
            <nav>
                <ul className="nav-links">
                    <li>
                        <a 
                            href="#work" 
                            className="nav-link"
                            onClick={(e) => {
                                e.preventDefault();
                                scrollToSection('work');
                            }}
                        >
                            WORK
                        </a>
                    </li>
                    <li>
                        <a 
                            href="#about" 
                            className="nav-link"
                            onClick={(e) => {
                                e.preventDefault();
                                scrollToSection('about');
                            }}
                        >
                            ABOUT
                        </a>
                    </li>
                    <li>
                        <a 
                            href="#recommendations" 
                            className="nav-link"
                            onClick={(e) => {
                                e.preventDefault();
                                scrollToSection('recommendations');
                            }}
                        >
                            RECOMMENDATIONS
                        </a>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

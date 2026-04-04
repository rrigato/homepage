import React, { useState, useEffect } from 'react';

export function SectionNav() {
    const [activeSection, setActiveSection] = useState('work');

    const sections = [
        { id: 'work', label: '01 Projects' },
        { id: 'about', label: '02 About' },
        { id: 'recommendations', label: '03 Recommendations' }
    ];

    useEffect(() => {
        const handleScroll = () => {
            const scrollPosition = window.scrollY + 100;
            
            for (const section of sections) {
                const element = document.getElementById(section.id);
                if (element) {
                    const { offsetTop, offsetHeight } = element;
                    if (scrollPosition >= offsetTop && scrollPosition < offsetTop + offsetHeight) {
                        setActiveSection(section.id);
                        break;
                    }
                }
            }
        };

        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    const scrollToSection = (sectionId) => {
        const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    return (
        <nav className="section-nav">
            {sections.map((section) => (
                <a
                    key={section.id}
                    href={`#${section.id}`}
                    className={`section-nav-item ${activeSection === section.id ? 'active' : ''}`}
                    onClick={(e) => {
                        e.preventDefault();
                        scrollToSection(section.id);
                    }}
                >
                    {section.label}
                </a>
            ))}
        </nav>
    );
}

import React from 'react';
import '../css/app.css';
import { Header } from './Header.jsx';
import { Hero } from './Hero.jsx';
import { Projects } from './Projects.jsx';
import { About } from './About.jsx';
import { BookRecommendations } from './BookRecommendations.jsx';
import { SectionNav } from './SectionNav.jsx';

export function App(){
    return(
        <div className='app'>
            <Header />
            <Hero />
            <SectionNav />
            <section id="work" className="section">
                <Projects />
            </section>
            <section id="about" className="section">
                <About />
            </section>
            <section id="recommendations" className="section">
                <BookRecommendations />
            </section>
        </div>
    );
}

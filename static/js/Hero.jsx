import React from 'react';

export function Hero() {
    const scrollToWork = () => {
        const element = document.getElementById('work');
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    };

    return (
        <section className="hero-section">
            <div className="hero-bg-effect"></div>
            <div className="hero-content">
                <h1 className="hero-title">
                    Welcome to Ryan's homepage, definitely not designed and built by the windsurf AI agent.
                </h1>
                <button className="cta-button" onClick={scrollToWork}>
                    VIEW MY WORK
                    <span>→</span>
                </button>
            </div>
            <div className="scroll-indicator">
                SCROLL TO EXPLORE
                <div className="scroll-icon">⌄</div>
            </div>
        </section>
    );
}

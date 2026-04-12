import React from 'react';
import aboutPhoto from '../img/aboutPhoto.jpg';

export function About() {
    return (
        <div>
            <div className="section-title">ABOUT ME</div>
            <h2 className="section-heading">Software engineer who enjoys reading and dedicating alarming amounts of energy to arguing with strangers on the internet</h2>

            <div className="about-content">
                <div className="about-text">

                    <p className="about-description">
                        I strive to be embarrassed by the quality of the architecture of any application I have built that is more than a year old. Endeavor to constantly be honing your craft.
                    </p>
                    <p className="about-description">
                        Check out the <a
                            href="https://web.archive.org/web/20240512053548/https://ryanrigato.com/"
                            target="_blank"
                            rel="noopener noreferrer"
                            style={{ color: '#4a9eff', textDecoration: 'none' }}
                        >
                            Wayback Machine archive
                        </a> of this site from a half a decade ago and remember the same developer was allowed to deploy to production.
                    </p>
                    <p className="about-description">
                        Look closely at my photo and you will notice that is not a clip on tie **drops mic and walks off stage**.
                    </p>
                    <a
                        href="https://github.com/rrigato/homepage"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="cta-button"
                    >
                        SOURCE CODE FOR THIS WEBSITE
                        <span>→</span>
                    </a>

                    <div className="social-links">
                        <a
                            href="https://github.com/rrigato"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="social-link"
                            title="GitHub"
                        >
                            GitHub
                        </a>
                        <a
                            href="https://linkedin.com/in/ryanrigato"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="social-link"
                            title="LinkedIn"
                        >
                            LinkedIn
                        </a>
                    </div>
                </div>

                <div className="about-photo-container">
                    <img
                        src={aboutPhoto}
                        alt="Ryan Rigato"
                        className="about-photo"
                    />
                </div>
            </div>
        </div>
    );
}
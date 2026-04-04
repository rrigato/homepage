import React from 'react';
import aboutPhoto from '../img/aboutPhoto.jpg';

export function About() {
    return (
        <div>
            <div className="section-title">ABOUT ME</div>
            <h2 className="section-heading">I'm a software engineer who loves solving complex problems.</h2>

            <div className="about-content">
                <div className="about-text">

                    <p className="about-description">
                        I strive to be embarrassed by the quality of the architecture of any application I have built that is more than a year old. Endeavor to constantly be honing your craft.
                    </p>
                    <p className="about-description">
                        Look closely at my photo and you will notice that is not a clip on tie **drops mic and walks off stage**.
                    </p>
                    <button className="cta-button">
                        GET TO KNOW ME
                        <span>→</span>
                    </button>

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
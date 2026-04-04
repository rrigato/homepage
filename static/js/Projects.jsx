import React, { useState } from 'react';

export function Projects() {
    const [activeProject, setActiveProject] = useState(0);

    const projects = [
        {
            id: 1,
            title: "Amazon Alexa Skill - Television Ratings",
            description: "Provides television ratings for the Adult Swim Saturday night Toonami television block.",
            applicationLink: "https://www.amazon.com/dp/B0B5596H7C/",
            sourceLink: "https://github.com/rrigato/tvratings"
        },
        {
            id: 2,
            title: "Air Quality Fuel Burning Restrictions",
            description: "Amazon Alexa skill to determine if a zip code has any fuel burning restrictions for heating your home.",
            applicationLink: "https://www.amazon.com/dp/B09PVD9VSC/",
            sourceLink: "https://github.com/rrigato/burnday"
        },
        {
            id: 3,
            title: "Web Scraper - TV Network Ratings",
            description: "Only location on the internet that has an archive of Adult Swim Toonami Ratings in a programmable format.",
            sourceLink: "https://github.com/rrigato/ratings"
        },
        {
            id: 4,
            title: "GitHub 3D Commit History",
            description: "Automates creation of 3D commit history to populate web application artifacts.",
            applicationLink: "https://github.com/rrigato/rrigato/blob/master/README.md",
            sourceLink: "https://github.com/rrigato/rrigato/"
        },
        {
            id: 5,
            title: "Markdown to HTML Converter",
            description: "Used to reduce documentation redundancy when hosting markdown documentation.",
            sourceLink: "https://github.com/rrigato/devdocs"
        }
    ];

    const scrollToProject = (index) => {
        setActiveProject(index);
        const container = document.querySelector('.carousel-container');
        if (container) {
            const firstCard = container.querySelector('.project-card');
            const cardWidth = firstCard ? firstCard.getBoundingClientRect().width + 30 : 430;
            container.scrollTo({
                left: index * cardWidth,
                behavior: 'smooth'
            });
        }
    };

    return (
        <div>
            <div className="section-title">WORK</div>
            <h2 className="section-heading">Featured Projects</h2>

            <div className="projects-carousel">
                <div className="carousel-container">
                    {projects.map((project, index) => (
                        <div key={project.id} className="project-card">
                            <div className="project-image">
                                {/* TODO: Add project images */}
                            </div>
                            <div className="project-content">
                                <h3 className="project-title">{project.title}</h3>
                                <p className="project-description">{project.description}</p>
                                <div className="project-links">
                                    {project.applicationLink && (
                                        <a
                                            href={project.applicationLink}
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            className="project-link"
                                        >
                                            View Project →
                                        </a>
                                    )}
                                    {project.sourceLink && (
                                        <a
                                            href={project.sourceLink}
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            className="project-link"
                                            style={{ marginLeft: project.applicationLink ? '20px' : '0' }}
                                        >
                                            Source Code →
                                        </a>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

                <div className="carousel-pagination">
                    {projects.map((_, index) => (
                        <button
                            key={index}
                            className={`pagination-dot ${activeProject === index ? 'active' : ''}`}
                            onClick={() => scrollToProject(index)}
                        >
                            {String(index + 1).padStart(2, '0')}
                        </button>
                    ))}
                </div>
            </div>
        </div>
    );
}

import React, { useState } from 'react';
import '../css/homepageSection.css';


/**homepage project details and links
 * 
 * @returns react jsx 
 */
export function Projects(){
    return(
        <div className='homepage-content'>
            <ul>
                <h3>Amazon Alexa Skill To retrieve Television Ratings</h3>
                <li>Provides television ratings for the Adult Swim Saturday night Toonami television block.</li>
                <li>
                    <a
                        href='https://www.amazon.com/dp/B0B5596H7C/'
                        target={'_blank'}
                    >
                        application link
                    </a>
                </li>
                <li>
                    <a
                        href='https://github.com/rrigato/tvratings'
                        target={'_blank'}
                    >
                        source code
                    </a>
                </li>

                <h3>Amazon Alexa Air Quality Caused Fuel Burning Restriction Skill</h3>
                <li>Amazon Alexa skill to determine if a zip code has any fuel burning restrictions for heating your home in the winter.</li>
                <li>
                    <a
                        href='https://www.amazon.com/dp/B09PVD9VSC/'
                        target={'_blank'}
                    >
                        application link
                    </a>
                </li>
                <li>
                    <a
                        href='https://github.com/rrigato/burnday'
                        target={'_blank'}
                    >
                        source code
                    </a>
                </li>

                <h3>Web scrapper television network ratings</h3>
                <li>Only location on the internet that has an archive of Adult Swim Toonami Ratings in a programmable format.</li>
                <li>Reach out to me on github if you would like access.</li>
                <li><sup><sup>First rule of building a sustainable web scraping application is to never build a web scrapping application.</sup></sup></li>
                <li>
                    <a
                        href='https://github.com/rrigato/ratings'
                        target={'_blank'}
                    >
                        source code
                    </a>
                </li>

                <h3>Github 3d commit history webpage</h3>
                <li>Automates creation of 3D commit history to populate web application artifacts.</li>
                <li>
                    <a
                        href='https://github.com/rrigato/rrigato/blob/master/README.md'
                        target={'_blank'}
                    >
                        application link
                    </a>
                </li>
                <li>
                    <a
                        href='https://github.com/rrigato/rrigato/'
                        target={'_blank'}
                    >
                        source code
                    </a>
                </li>

                <h3>Markdown to html converter</h3>
                <li>Used to reduce documentation redundancy when hosting markdown documentation</li>
                <li>
                    <a
                        href='https://github.com/rrigato/devdocs'
                        target={'_blank'}
                    >
                        source code
                    </a>
                </li>
            </ul>

        </div>
    );
}
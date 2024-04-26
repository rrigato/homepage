import React from 'react';
import '../css/homepageSection.css';
import aboutPhoto from '../img/aboutPhoto.jpg';

/**Details about the website
 *
 * @returns react jsx
 */
export function About(){
    return(
        <div className='homepage-content'>
            <div>
                <ul>
                    <h3>What do I need to know about this website?</h3>
                    <li>Website
                        <a
                            href='https://github.com/rrigato/homepage'
                            target={'_blank'}
                        >source code </a>
                    </li>
                    <li>I strive to be embarrassed by the quality of the architecture of any application I have built that is more than a year old. </li>
                    <li>Endeavor to constantly be honing your craft.</li>
                    <li>How do you practice your skills in the same way a musician practices cords?</li>

                    <li>This webiste went from a Java EE2 web app hosted in google app engine
                        all the way to a serverless web app deployed to AWS</li>
                    <li>Run a <code>git log --before="2018-01-01"</code> on the source code for a stroll down memory lane!</li>

                    <li>The world's largest tuned mass damper is at the
                        <a
                            href='https://en.wikipedia.org/wiki/Tuned_mass_damper'
                            target={'_blank'}
                        >Taipei 101</a>
                    </li>
                    <h3>Obilgatory socially awkard photo of the engineer who built this website?</h3>
                    <div>
                        <img
                            alt='Image of website author'
                            src={aboutPhoto}

                        ></img>
                    </div>
                </ul>
            </div>
        </div>
    );
}
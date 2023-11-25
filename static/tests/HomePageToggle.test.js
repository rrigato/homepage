import { render } from '@testing-library/react';
import { userEvent } from '@testing-library/user-event';
import { About } from '../js/About.jsx';
import { BookRecommendations } from '../js/BookRecommendations.jsx';
import { HomePageToggle } from '../js/HomePageToggle.jsx';
import { Projects } from '../js/Projects.jsx';

jest.mock('../js/About.jsx');
jest.mock('../js/BookRecommendations.jsx');
jest.mock('../js/Projects.jsx');

describe('Central Content for site', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });
      
    test('HomePageToggle default render', async () => {
        Projects.mockReturnValue(<div>mock-projects-component</div>);
        About.mockReturnValue(<div>mock-about-component</div>);
        
        
        const {findByRole} = render(<HomePageToggle/>);

        
        await findByRole(
            'button', {name: 'About'}
        );
        await findByRole(
            'button', {name: 'Projects'}
        );
        await findByRole(
            'button', {name: 'Book Recommendations'}
        );
        expect(Projects).toHaveBeenCalled()

    });

    test('About component called when clicked', async () => {
        const userStep = userEvent.setup();
        Projects.mockReturnValue(<div>mock-projects-component</div>);
        About.mockReturnValue(<div>mock-about-component</div>);

        
        const {findByRole} = render(<HomePageToggle/>);

        
        const aboutButton = await findByRole(
            'button', {name: 'About'}
        );
        await userStep.click(aboutButton);
        expect(About).toHaveBeenCalled()

    });

    test('BookRecommendations component called when clicked', async () => {
        const userStep = userEvent.setup();
        Projects.mockReturnValue(<div>mock-projects-component</div>);
        About.mockReturnValue(<div>mock-about-component</div>);
        BookRecommendations.mockReturnValue(
            <div>mock-book-recommendations-component</div>
        );

        
        const {findByRole} = render(<HomePageToggle/>);

        
        const bookRecommendationsButton = await findByRole(
            'button', {name: 'Book Recommendations'}
        );
        await userStep.click(bookRecommendationsButton);
        expect(BookRecommendations).toHaveBeenCalled()

    });
});
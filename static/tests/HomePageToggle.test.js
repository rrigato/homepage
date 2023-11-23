import { render } from '@testing-library/react';
import { userEvent } from '@testing-library/user-event';
import { About } from '../js/About.jsx';
import { HomePageToggle } from '../js/HomePageToggle.jsx';
import { Projects } from '../js/Projects.jsx';

jest.mock('../js/About.jsx');
jest.mock('../js/Projects.jsx');

describe('Central Content for site', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });
      
    test('HomePageToggle default render', async () => {
        Projects.mockReturnValue(<div>mock-projects</div>);

        
        
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

    test('About component  default render', async () => {
        const userStep = userEvent.setup();
        Projects.mockReturnValue(<div>mock-projects</div>);
        About.mockReturnValue(<div>mock-about</div>);

        
        
        const {findByRole} = render(<HomePageToggle/>);

        
        const aboutButton = await findByRole(
            'button', {name: 'About'}
        );

        await userStep.click(aboutButton);
        expect(About).toHaveBeenCalled()

    });
});
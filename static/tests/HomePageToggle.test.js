import { render } from '@testing-library/react';
import { HomePageToggle } from '../js/HomePageToggle.jsx';
import { Projects } from '../js/Projects.jsx';

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
});
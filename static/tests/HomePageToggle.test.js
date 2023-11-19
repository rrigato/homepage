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

        
        
        const {getByRole} = render(<HomePageToggle/>);

        
        getByRole(
            'button', {name: 'About'}
        );
        getByRole(
            'button', {name: 'Projects'}
        );
        getByRole(
            'button', {name: 'Book Recommendations'}
        );

        expect(Projects).toHaveBeenCalled()

    });
});
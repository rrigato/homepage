import { render } from '@testing-library/react';
import { HomePageToggle } from '../js/HomePageToggle.jsx';

describe('Central Content for site', () => {
    test('HomePageToggle default render', async () => {
        
        
        const {getByRole} = render(<HomePageToggle/>);

        
        const aboutButton = await getByRole(
            'button', {name: 'About'}
        );
        const projectButton = await getByRole(
            'button', {name: 'Projects'}
        );
        const bookRecommendationsButton = await getByRole(
            'button', {name: 'Book Recommendations'}
        );


    });
});
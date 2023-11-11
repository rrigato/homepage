import { render } from '@testing-library/react';
import { HomePageToggle } from '../js/HomePageToggle.jsx';

describe('Central Content for site', () => {
    test('HomePageToggle default render', () => {
        
        
        const {findByText} = render(<HomePageToggle/>);

        
        findByText(RegExp('Latest Projects'));

    });
});
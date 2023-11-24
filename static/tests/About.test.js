import {  render } from '@testing-library/react';
import { About } from '../js/About.jsx';


describe('About displayed on screen', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });
      
    test('About section', async () => {        
        

        const {getAllByRole} = render(<About/>);

        
        const numProjectHeaders = getAllByRole(
            'heading'
        );
        const aboutImage = getAllByRole(
            'img'
        );
    });
});
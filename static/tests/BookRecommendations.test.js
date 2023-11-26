import {  render } from '@testing-library/react';
import { BookRecommendations } from '../js/BookRecommendations.jsx';


describe('BookRecommendations displayed on screen', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });
      
    test('BookRecommendations section', async () => {        
        

        const {getAllByRole, getByRole} = render(<BookRecommendations/>);

        
        const bookLinks = getAllByRole(
            'link'
        );
        const numHeaders = getAllByRole(
            'heading'
        );
        expect(bookLinks.length).toBe(4);
        expect(numHeaders.length).toBe(2);

    });
});
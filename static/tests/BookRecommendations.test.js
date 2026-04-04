import {  render } from '@testing-library/react';
import { BookRecommendations } from '../js/BookRecommendations.jsx';


describe('BookRecommendations displayed on screen', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });

    test('BookRecommendations section', async () => {

        const {getAllByRole, getByRole} = render(<BookRecommendations/>);

        const numHeaders = getAllByRole('heading');
        const numButtons = getAllByRole('button');

        // Should have 9 headings (1 main heading + 8 book titles)
        expect(numHeaders.length).toBe(9);
        // Should have 9 buttons (1 CTA + 8 pagination)
        expect(numButtons.length).toBe(9);

    });
});
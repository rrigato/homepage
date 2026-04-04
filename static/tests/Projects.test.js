import {  render } from '@testing-library/react';
import { Projects } from '../js/Projects.jsx';


describe('Projects displayed on screen', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });

    test('Number of project sections', async () => {

        const {getAllByRole} = render(<Projects/>);

        const numHeaders = getAllByRole('heading');
        const numButtons = getAllByRole('button');

        // Should have 6 headings (1 main heading + 5 project titles)
        expect(numHeaders.length).toBe(6);
        // Should have 5 pagination buttons
        expect(numButtons.length).toBe(5);
    });
});
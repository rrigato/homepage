import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { About } from '../js/About.jsx';


describe('About displayed on screen', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });

    test('About section', async () => {

        const {getAllByRole, getByRole} = render(<About/>);

        const numHeaders = getAllByRole('heading');
        const aboutImage = getByRole('img');
        const numButtons = getAllByRole('button');

        // Should have 1 heading (main heading)
        expect(numHeaders.length).toBe(1);
        // Should have the about image
        expect(aboutImage).toBeInTheDocument();
        // Should have 1 CTA button
        expect(numButtons.length).toBe(1);
    });
});
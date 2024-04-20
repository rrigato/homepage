import {  render } from '@testing-library/react';
import { Projects } from '../js/Projects.jsx';


describe('Projects displayed on screen', () => {
    afterEach(() => {
        jest.resetAllMocks();
    });

    test('Number of project sections', async () => {


        const {getAllByRole} = render(<Projects/>);

        getAllByRole('heading', {level: 2});
        const numProjectHeaders = getAllByRole(
            'heading'
        );
        expect(numProjectHeaders.length).toBe(5);
    });
});
import { render } from '@testing-library/react';
import { App } from '../js/App.jsx';
import { HomePageToggle } from '../js/HomePageToggle.jsx';

jest.mock('../js/HomePageToggle.jsx');

describe('entry point for app', () => {

    afterEach(() => {
        jest.resetAllMocks();
    });

    test('HomePageToggle called', () => {
        
        
        const renderedHomepage = render(<App/>);

        expect(HomePageToggle).toHaveBeenCalled();

    });
});
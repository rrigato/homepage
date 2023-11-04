import { render } from '@testing-library/react';
import {App} from '../App.jsx';

describe('entry point for app', () => {
    /**
     * @jest-environment jsdom
     */
    test('HomePageToggle called', () => {
        
        
        const renderedHomepage = render(<App/>);


        renderedHomepage.findByText('react initial setup');

    });
});
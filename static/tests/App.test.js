import { render } from '@testing-library/react';
import { App } from '../js/App.jsx';

describe('entry point for app', () => {
    test('HomePageToggle called', () => {
        
        
        const renderedHomepage = render(<App/>);

        // TODO - next step call HomePageToggle component
        renderedHomepage.findByText('initial homepage setup');

    });
});
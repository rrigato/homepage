import { render } from '@testing-library/react';
import { App } from '../js/App.jsx';
import { Header } from '../js/Header.jsx';
import { Hero } from '../js/Hero.jsx';
import { SectionNav } from '../js/SectionNav.jsx';

jest.mock('../js/Header.jsx');
jest.mock('../js/Hero.jsx');
jest.mock('../js/SectionNav.jsx');

describe('entry point for app', () => {

    afterEach(() => {
        jest.resetAllMocks();
    });

    test('All components rendered', () => {

        const renderedHomepage = render(<App/>);

        expect(Header).toHaveBeenCalled();
        expect(Hero).toHaveBeenCalled();
        expect(SectionNav).toHaveBeenCalled();

    });
});
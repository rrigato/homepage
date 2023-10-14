import React from 'react';
import { createRoot } from 'react-dom/client';



const root = createRoot(
    document.getElementById('app-entry-point')
);
root.render(<h1>react initial setup</h1>);
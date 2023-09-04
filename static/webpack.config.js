const path = require('path');

module.exports = {
    entry: './app.jsx',
    output: {
        filename: 'index.js',
        path: path.resolve(__dirname, 'dist'),
    },
};
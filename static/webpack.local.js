const { merge } = require('webpack-merge');
const baseConfig = require('./webpack.config.js');
const path = require('path');

module.exports = merge(
    baseConfig,
    
    {
        devServer: {
            static: {
                directory: path.join(
                    __dirname, 'static', 'dist'),
            },
            open: true
        },
        mode: 'development'
    }
);

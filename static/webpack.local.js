const { merge } = require('webpack-merge');
const baseConfig = require('./webpack.config.js');
const path = require('path');

module.exports = merge(
    baseConfig,
    
    {
        devServer: {
            open: true
        },
        mode: 'development'
    }
);

const { merge } = require('webpack-merge');
const baseConfig = require('./webpack.config.js');

module.exports = merge(
    baseConfig,
    
    {
        devServer: {
            open: true
        },
        mode: 'development'
    }
);

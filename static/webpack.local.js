const { merge } = require('webpack-merge');
const baseConfig = require('./webpack.config.js');

module.exports = merge(
    baseConfig,
    
    {
        devServer: {
            static: {
                directory: path.join(__dirname, 'dist'),
            },
            open: true
        },
        mode: 'development'
    }
);

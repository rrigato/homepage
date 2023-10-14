const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
    entry: './js/index.js',
    module: {
        rules: [
            {
                test: /\.html$/i,
                loader: 'html-loader',
            },
            {
                test: /\.(?:js|cjs)$/,
                exclude: /node_modules/,
                use: {
                  loader: 'babel-loader',
                  options: {
                    presets: [
                        '@babel/preset-react'
                    ]
                  }
                }
            }
        ],
    },
    
    plugins: [
        new HtmlWebpackPlugin({
            template: 'index.html'
        })
    ],
};
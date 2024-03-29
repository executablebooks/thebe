const path = require('path');
const { DefinePlugin, NormalModuleReplacementPlugin } = require('webpack');

const shimJS = path.resolve(__dirname, 'src', 'empty.js');
function shim(regExp) {
  return new NormalModuleReplacementPlugin(regExp, shimJS);
}

module.exports = {
  optimization: {
    usedExports: true,
  },
  entry: {
    app: './src/thebe/entrypoint.ts',
  },
  plugins: [shim(/\.(svg|ttf|eot|woff2|woff)/), new DefinePlugin({ 'process.env': {} })],
  output: {
    filename: 'thebe-core.min.js',
    path: path.resolve(__dirname, 'dist', 'lib'),
    publicPath: '/',
  },
  module: {
    rules: [
      {
        resourceQuery: /raw/,
        type: 'asset/source',
      },
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        loader: 'ignore-loader',
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
};

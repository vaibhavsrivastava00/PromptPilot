// esbuild.js
const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['src/extension.ts'],
  bundle: true,
  outdir: 'dist',
  platform: 'node',
  external: ['vscode'], // Don't bundle VS Code API
  sourcemap: true,
  format: 'cjs',
  target: 'es2020'
}).catch(() => process.exit(1));

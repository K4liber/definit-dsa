import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const defsRoot = path.resolve(__dirname, '../src/definit_db/data_md/definitions');

export default defineConfig({
  base: '/definit-db/',
  server: {
    port: 5173,
    fs: {
      allow: [path.resolve(__dirname, '..')],
    },
  },
  plugins: [
    react(),
    {
      name: 'serve-definitions-md',
      configureServer(server) {
        server.middlewares.use('/md', async (req, res, next) => {
          try {
            const rawUrl = req.url ?? '';
            const urlPath = rawUrl.split('?')[0] ?? '';
            const rel = decodeURIComponent(urlPath).replace(/^\//, '');

            // Only allow .md reads
            if (!rel.endsWith('.md')) {
              res.statusCode = 400;
              res.setHeader('Content-Type', 'text/plain; charset=utf-8');
              res.end('Expected a .md path');
              return;
            }

            const full = path.resolve(defsRoot, rel);
            const relToRoot = path.relative(defsRoot, full);
            if (relToRoot.startsWith('..') || path.isAbsolute(relToRoot)) {
              res.statusCode = 403;
              res.setHeader('Content-Type', 'text/plain; charset=utf-8');
              res.end('Forbidden');
              return;
            }

            const buf = await fs.readFile(full);
            res.statusCode = 200;
            res.setHeader('Content-Type', 'text/markdown; charset=utf-8');
            res.end(buf);
          } catch (e) {
            // fall through to Vite (will typically return index.html)
            next();
          }
        });
      },
    },
  ],
});

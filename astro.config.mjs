import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

/** GitHub Pages project site — only host we use right now */
const SITE = 'https://havpen.github.io';
const BASE = '/StationOneCafe';

export default defineConfig({
  site: SITE,
  base: BASE,
  trailingSlash: 'always',
  compressHTML: true,
  integrations: [
    sitemap({
      filter: (page) => !page.includes('404'),
      changefreq: 'weekly',
      priority: 1,
      lastmod: new Date(),
    }),
  ],
  build: {
    inlineStylesheets: 'auto',
  },
  vite: {
    plugins: [tailwindcss()],
    build: {
      cssMinify: true,
      assetsInlineLimit: 2048,
    },
  },
});

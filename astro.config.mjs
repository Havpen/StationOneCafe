import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

/** GitHub Actions → project Pages; Netlify / local → site root */
const isGitHubPages = process.env.GITHUB_ACTIONS === 'true';

const SITE = isGitHubPages
  ? 'https://havpen.github.io'
  : 'https://stationonecafe.netlify.app';

const BASE = isGitHubPages ? '/StationOneCafe' : '/';

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

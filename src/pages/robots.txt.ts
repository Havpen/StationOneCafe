import type { APIRoute } from 'astro';

export const prerender = true;

const site = (import.meta.env.SITE || 'https://stationonegomel.by').replace(/\/$/, '');

export const GET: APIRoute = () => {
  const body = `User-agent: *
Allow: /

Disallow: /404
Disallow: /404.html

Sitemap: ${site}/sitemap-index.xml
`;

  return new Response(body, {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};

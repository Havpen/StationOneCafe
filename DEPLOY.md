# Деплой Station One Cafe

Статический Astro-сайт. Папка публикации: **`dist/`**.

## 1. Домен (обязательно)

В `astro.config.mjs` задай реальный URL:

```js
const SITE = 'https://ваш-домен.by';
```

От него зависят canonical, Open Graph, JSON-LD, `robots.txt` и sitemap.

## 2. Сборка

```bash
npm ci
npm run build
npm run preview   # проверка локально: http://localhost:4321
```

Node **≥ 20**.

## 3. Хостинг (любой)

| Платформа | Как |
|-----------|-----|
| **Vercel** | Import проекта → Framework Astro / Output `dist`. Конфиг: `vercel.json` |
| **Netlify** | Build `npm run build`, publish `dist`. Конфиг: `netlify.toml` |
| **Cloudflare Pages** | Build `npm run build`, output `dist`. Есть `public/_headers` и `_redirects` |

После деплоя включи **HTTPS** и редирект `www` → apex (или наоборот).

## 4. После выкладки

1. Открыть сайт, проверить меню, якоря, карту, `tel:`  
2. `https://ваш-домен/robots.txt` и `…/sitemap-index.xml`  
3. [Google Search Console](https://search.google.com/search-console) — добавить ресурс + sitemap  
4. [Яндекс.Вебмастер](https://webmaster.yandex.ru/) — то же  
5. [Rich Results Test](https://search.google.com/test/rich-results) — JSON-LD  
6. PageSpeed Insights  

## Не деплоится

`source-media/`, `node_modules/`, корневые `*-upscaled.png` — в `.gitignore`, в `dist` не попадают.

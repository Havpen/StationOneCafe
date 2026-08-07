# Деплой Station One Cafe

Статический Astro-сайт. Папка публикации: **`dist/`**.

## 1. Домен

В `astro.config.mjs`:

- **Netlify / локально:** `site = https://stationonecafe.netlify.app`, `base = /`
- **GitHub Actions:** `site = https://havpen.github.io`, `base = /StationOneCafe`

От них зависят canonical, Open Graph, JSON-LD, `robots.txt` и sitemap.

URL:
- Netlify: https://stationonecafe.netlify.app/
- GitHub Pages: https://havpen.github.io/StationOneCafe/

При своём домене обнови `site` в `astro.config.mjs`.

## 2. Сборка

```bash
npm ci
npm run build
npm run preview   # проверка локально
```

С `base: '/'` локально открывай `http://localhost:4321/` (`trailingSlash: 'always'`).

Node **≥ 20**.

## 3. GitHub Pages (основной хостинг)

Деплой через Actions: [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml) → ветка **`gh-pages`**.

### Однократная настройка

1. Дождись зелёного workflow **Deploy GitHub Pages** в **Actions** (создаст ветку `gh-pages`)
2. Репозиторий → **Settings → Pages**
3. **Build and deployment → Source:** Deploy from a branch
4. **Branch:** `gh-pages` / `/ (root)` → Save
5. Через 1–2 минуты открой https://havpen.github.io/StationOneCafe/

Конфиги Netlify / Vercel остаются опциональными запасными вариантами.

## 4. Другой хостинг (опционально)

| Платформа | Как |
|-----------|-----|
| **Vercel** | Import проекта → Framework Astro / Output `dist`. Конфиг: `vercel.json` |
| **Netlify** | Build `npm run build`, publish `dist`. Конфиг: `netlify.toml` |
| **Cloudflare Pages** | Build `npm run build`, output `dist`. Есть `public/_headers` и `_redirects` |

На корневом домене без подпути убери или смени `base` в `astro.config.mjs` на `/`.

После деплоя включи **HTTPS** и редирект `www` → apex (или наоборот).

## 5. После выкладки

1. Открыть сайт, проверить меню, якоря, карту, `tel:`
2. `https://havpen.github.io/StationOneCafe/robots.txt` и `…/sitemap-index.xml`
3. [Google Search Console](https://search.google.com/search-console) — добавить ресурс + sitemap
4. [Яндекс.Вебмастер](https://webmaster.yandex.ru/) — то же
5. [Rich Results Test](https://search.google.com/test/rich-results) — JSON-LD
6. PageSpeed Insights

## Не деплоится

`source-media/`, `node_modules/`, корневые `*-upscaled.png` — в `.gitignore`, в `dist` не попадают.

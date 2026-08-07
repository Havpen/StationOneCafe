# Деплой Station One Cafe

Статический Astro-сайт. Хостинг: **GitHub Pages**. Папка публикации: **`dist/`**.

## 1. Домен

В `astro.config.mjs`:

```js
site: 'https://havpen.github.io'
base: '/StationOneCafe'
```

От них зависят canonical, Open Graph, JSON-LD, `robots.txt` и sitemap.

Сайт: **https://havpen.github.io/StationOneCafe/**

При своём домене обнови `site` / `base` в `astro.config.mjs`.

## 2. Сборка и локальный просмотр

```bash
npm ci
npm run build
npm run dev
```

С `base: '/StationOneCafe'` открывай: **http://localhost:4321/StationOneCafe/**

Node **≥ 20**.

## 3. GitHub Pages

Деплой через Actions: [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml) → ветка **`gh-pages`**.

### Однократная настройка

1. Push в `main` → дождись зелёного workflow **Deploy GitHub Pages**
2. Репозиторий → **Settings → Pages**
3. **Source:** Deploy from a branch
4. **Branch:** `gh-pages` / `/ (root)` → **Save**
5. Открой https://havpen.github.io/StationOneCafe/

Custom domain пока не нужен — поле оставь пустым.

## 4. После выкладки

1. Проверить меню, якоря, карту, `tel:`
2. `https://havpen.github.io/StationOneCafe/robots.txt` и `…/sitemap-index.xml`
3. Google Search Console / Яндекс.Вебмастер — sitemap на этот URL

## Не деплоится

`source-media/`, `node_modules/`, корневые `*-upscaled.png` — в `.gitignore`, в `dist` не попадают.

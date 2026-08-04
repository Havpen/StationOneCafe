# SEO-карта (ТЗ для разработчика) — Station One Cafe

Одностраничный лендинг: **один интент визита/заказа** закрывается блоками на `/`.  
Источник ключей: `seo/semantic-core.md`.

| URL | Главный ключ (H1/блок) | Title (~60) | Description (~160) | LSI / вторичные | Блок |
|-----|------------------------|-------------|--------------------|-----------------|------|
| `/` | Station One Cafe — кафе и ресторан в Гомеле | Station One Cafe — кафе и кальяны в Гомеле | Station One Cafe — кафе и кальян-бар в Гомеле, ул. Советская 29А. Меню, кальяны, доставка. Забронируйте стол: +375 33 333-52-33. | кафе Гомель, ресторан Гомель, Стэйшн Уан | Hero `#top` |
| `/#kitchen` | Меню / кухня кафе Гомель | — (якорь) | — | меню кафе гомель, бизнес ланч, пицца* | Kitchen |
| `/#gallery` | Галерея / атмосфера | — | — | уютное кафе гомель | Gallery |
| `/#hookah` | Кальян Гомель / кальян-бар | — | — | кальяны гомель, кальян кафе | Hookah |
| `/#delivery` | Доставка еды Гомель / заказать | — | — | яндекс еда, just eat | Delivery |
| `/#reviews` | Отзывы | — | — | опыт клиента | Reviews |
| `/#map` | Как нас найти / адрес | — | — | кафе гомель адрес, советская 29а, как добраться | Map |
| `/#contacts` | Забронировать стол Гомель | — | — | бронь стола, телефон | Book |
| `/#faq` | FAQ (только JSON-LD) | — | — | бронь, адрес, доставка, кальян | `faqs` в `site.ts` → Layout |

\*Только при наличии в меню.

## Мета главной (внедрено в `src/data/site.ts` + Layout)

- **H1:** Station One (+ скрытый хвост для робота: Cafe — кафе и ресторан в Гомеле)
- **Canonical:** `SITE_URL/`
- **OG/Twitter:** да
- **JSON-LD:** Restaurant/CafeOrCoffeeShop + FAQPage + BreadcrumbList + Reviews

## Техчеклист регламента (статус)

| Пункт | Статус |
|-------|--------|
| СЯ + фильтрация | ✅ `seo/semantic-core.md` |
| SEO-карта | ✅ этот файл |
| header/main/footer/nav/section | ✅ |
| Один H1 | ✅ |
| H2 по секциям | ✅ |
| Title / Description / Canonical | ✅ |
| robots.txt + sitemap.xml | ✅ |
| Open Graph | ✅ |
| LocalBusiness / Restaurant JSON-LD | ✅ |
| FAQPage | ✅ |
| AggregateRating / Review | ✅ |
| Breadcrumbs JSON-LD | ✅ |
| 404 | ✅ |
| WebP + lazy + LCP hero | ✅ |
| font-display: swap | ✅ (fontsource) |
| Cache-Control assets | ✅ |
| alt у изображений | ✅ доработано |
| HTTPS / www | ⚙️ на хостинге при деплое |
| GSC / Вебмастер | ⚙️ после деплоя |

## После деплоя

1. Прописать реальный домен в `src/data/site.ts`, `astro.config.mjs`, `robots.txt`, `sitemap.xml`.  
2. Google Search Console + Яндекс.Вебмастер.  
3. Rich Results Test / Schema Validator.  
4. PageSpeed Insights (цель 90+).

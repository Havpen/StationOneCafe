/** Production domain from astro.config `site` (change there before deploy) */
export const SITE_URL = (import.meta.env.SITE || 'https://stationonegomel.by').replace(
  /\/$/,
  '',
);

export const site = {
  name: 'Station One Cafe',
  shortName: 'Station One',
  tagline: 'Кафе, ресторан и кальяны в Гомеле',
  /** ~150–160 символов для snippet */
  description:
    'Station One Cafe — кафе и кальян-бар в Гомеле, ул. Советская 29А. Меню, кальяны, доставка. Забронируйте стол: +375 33 333-52-33.',
  locale: 'ru_BY',
  language: 'ru',
  phone: '+375333335233',
  phoneDisplay: '+375 33 333-52-33',
  address: {
    street: 'ул. Советская, 29А, 2 этаж',
    city: 'Гомель',
    region: 'Гомельская область',
    country: 'BY',
  },
  geo: {
    latitude: 52.4347,
    longitude: 31.0095,
  },
  /** Ежедневно 12:00–01:00 (по данным карточки заведения) */
  openingHours: ['Mo-Su 12:00-01:00'],
  openingHoursDisplay: 'ежедневно, 12:00–01:00',
  social: {
    instagram: 'https://www.instagram.com/station_one_gomel/',
    yandexMaps: 'https://yandex.by/maps/-/CTCHBF1p',
    yandexOrg: 'https://yandex.by/maps/org/112602723149/',
    yandexEda: 'https://eda.yandex.by/r/station_one',
    justEat: 'https://just-eat.by/station-one-gomel',
  },
  /** Рейтинг с публичной карточки Яндекс (ориентир) */
  rating: {
    value: 4.4,
    count: 509,
    best: 5,
  },
  logo: '/logo.webp',
  ogImage: '/assets/hero.webp',
  themeColor: '#212226',
} as const;

/** Title ~60 символов */
export const pageTitle = 'Station One Cafe — кафе и кальяны в Гомеле';

export const faqs = [
  {
    question: 'Как забронировать стол в Station One Cafe?',
    answer:
      'Позвоните по телефону +375 33 333-52-33. Назовите дату, время и количество гостей — администратор подтвердит бронь.',
  },
  {
    question: 'Где находится Station One Cafe в Гомеле?',
    answer:
      'Гомель, ул. Советская, 29А, 2 этаж. Маршрут удобно построить в Яндекс Картах.',
  },
  {
    question: 'Как добраться до Station One?',
    answer:
      'Мы в центре Гомеля на Советской, 29А (2 этаж). Откройте точку на Яндекс Картах и постройте маршрут от вашего адреса.',
  },
  {
    question: 'Есть ли доставка еды из Station One?',
    answer:
      'Да. Заказать меню можно через Яндекс Еду и Just Eat — Station One Cafe уже в приложении.',
  },
  {
    question: 'Есть ли кальяны в Station One Cafe?',
    answer:
      'Да, в Station One есть кальянная карта: Classic, Medium и Premium. Можно совместить с ужином и встречей.',
  },
] as const;

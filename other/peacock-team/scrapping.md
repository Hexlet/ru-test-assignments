> Локальная копия. Источник: <https://github.com/PeacockTeam/new-job>

Написать node-js скрипт на базе Puppeteer, осуществляющий сбор объявлений с авито.

Входные данные - ссылка на страницу с объявлениями (например, <https://www.avito.ru/sankt-peterburg/koshki/poroda-meyn-kun-ASgBAgICAUSoA5IV>)

Результат - json файл с массивом объявлений

```typescript
interface Advert {
  title: string;
  description: string;
  url: string;
  price: number;
  author: string;
  date: string; // ISO-8601
  phone: string;
}
```

Задачи по symfony:

# 1. Реализовать две сущности: Категория, Товар с следующими полями

Category:

* id (int)
* title (string length min: 3, max 12)
* eId (int|null)

Product:

* id (int)
* categories (связь: ManyToMany)
* title (string length min: 3, max 12)
* price (float range min: 0, max 200)
* eId (int|null)

*eId – произвольный id из любой другой системы

## 2. Реализовать CRUD контроллер и сервис для сущности Product

Логика добавления, удаления должна быть вынесена в сервис, данные методы также использовать в задаче #3.

## 3. Реализовать консольную команду, которая читает два нижеприведенных файла Json и добавляет/обновляет записи в БД

categories.json:
[
 {"eId": 1, "title": "Category 1"},
 { "eId": 2,"title": "Category 2"},
 { "eId": 2,"title": "Category 33333333"}
]

products.json
[
 {"eId": 1, "title": "Product 1", "price": 101.01, "categoriesEId": [1,2]},
 {"eId": 2, "title": "Product 2", "price": 199.01, "categoryEId": [2,3]},
 {"eId": 3, "title": "Product 33333333", "price": 999.01, "categoryEId": [3,1]}
]

*учесть валидацию данных

## 4. Реализовать подписчик/слушатель на добавление/изменение product

Подписчик или слушатель при обновление/добавление данных о продукте должен отправлять сообщение на email указанный в параметре (произвольное название) в .env файл

Выполненное задание присылай на почту <webprog01@tmktools.ru>

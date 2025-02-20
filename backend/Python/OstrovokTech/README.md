## Тестовые задания для Python

### Задача 1: Что может быть проще SQL?

Вам дана таблица в postgres, которая представляет из себя список сотрудников с их зарплатами и отделами.
Необходимо написать запрос, который будет выбирать человека с максимальной зарплатой из каждого отдела. В качестве тестовых данных можете использовать [дамп таблицы](employee.sql), пример схемы:
```
postgres=# \d employee
            Table "public.employee"
   Column   |         Type          | Modifiers
------------+-----------------------+-----------
 id         | integer               | not null
 name       | character varying(30) |
 department | character varying(30) |
 salary     | integer               |
Indexes:
    "employee_pkey" PRIMARY KEY, btree (id)
```
Если нам нужна информация о всех сотрудниках, имеющих максимальную зарплату в отделе(в случае, когда она одинаковая):
```
SELECT m.name, m.department, t.mx FROM (SELECT department, max(salary) as mx from employee GROUP BY department) t JOIN employee m on m.department = t.department and t.mx = m.salary;
```
Если достаточно информации о любом из сотрудников с максимальной зарплатой:
```
SELECT DISTINCT ON (department) department, name, salary from employee ORDER BY department, salary DESC;
```
Запустить запросы, посмотреть результ:
```
make sql
```


### Задача 2: Smashing Wallpaper Downloader

Есть прекрасный сайт Smashing Magazine, который каждый месяц выкладывает отличные обои для десктопа. Заходить каждый месяц и проверять, что там нового дело не благородное, поэтому давайте попробуем автоматизировать эту задачу.
Требуется написать cli утилиту, которая будет качать все обои в требуемом разрешение за указанный месяц-год в текущую директорию пользователя. Вот [тут](https://www.smashingmagazine.com/tag/wallpapers/) находятся все обои, а [здесь](https://www.smashingmagazine.com/2017/04/desktop-wallpaper-calendars-may-2017/) находятся обои за май 2017.

Условия:
* Python 3.5+
* Любые сторонние библиотеки
* PEP8
* Если останется время, то можете покрыть её тестами с помощью py.test (:

Подготовить среду, установить зависимости(откроет консоль внутри контейнера)
```
make getwallpapers_env
```
Запустить скрипт загрузки обоев в консоли из предыдущей команды:
```
./getwallpapers.py 022018 640x480
```
Запустить тесты
```
make getwallpapers_test
```
Особенности:
* Если обои доступны в вариантах с календарём и без, утилита скачает оба.
* Не все обои доступны во всех разрешениях, если конкретных обоев запрошенного разрешения нет, утилита их пропустит.

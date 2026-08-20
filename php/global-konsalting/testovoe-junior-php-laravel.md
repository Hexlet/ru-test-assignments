> Локальная копия. Источник: <https://docs.google.com/document/d/1fl4eCKdpSXUNyu899NCKaDy_fdHcVPDE-GoO9siZPX4/edit>

2023-07 Тестовое задание для PHP-разработчика (Laravel)

Разработать функционал на Laravel c базой данных PostgreSQL.

Реализовать вывод списка продуктов, просмотр карточки продукта, добавление,  редактирование и удаление продукта.

Создать таблицу «products».

ID

uint, autoincrement

ARTICLE

varchar(255), unique index

NAME

varchar(255)

STATUS

varchar(255)

"available" | "unavailable"

DATA

jsonb

несколько разных полей
(например, Color и Size)
на своё усмотрение

timestamps

soft deletes

Создать Eloquent-модель «Product», связанную с таблицей «products».

В модели реализовать Local Scope для получения только доступных продуктов (STATUS = “available”).

Сделать валидацию создания и редактирования:

NAME — обязательное поле, длиной не менее 10 символов;

ARTICLE — обязательное поле, только латинские символы и цифры, уникальное в таблице.

Создать роль администратора, который может редактировать артикул, остальным пользователям можно редактировать всё, кроме артикула.

Роль пользователя можно узнать из настроек (config(‘products.role’)).

Реализовать валидацию и проверку прав (контроллер, модель, отдельный сервис — на своё усмотрение).

Дополнительно:

При создании продукта реализовать отправку на заданный в конфигурации Email (config(‘products.email’)) уведомления (Notification) о том, что продукт создан.

Уведомление должно отправляться через задачу (Job) в очереди (Queue).

Готовое приложение упаковать в docker.

Интерфейс приложения реализовать соответственно макету (см. ссылку): [https://www.figma.com/file/pVspJcvzwZUYynT2dogGG2/PIN-ERP-ТЗ-03.02.2022-(Copy)?type=design&node-id=0-1&mode=design&t=pzPc1ZJlca6HnPL3-0](https://www.google.com/url?q=https://www.figma.com/file/pVspJcvzwZUYynT2dogGG2/PIN-ERP-%25D0%25A2%25D0%2597-03.02.2022-(Copy)?type%3Ddesign%26node-id%3D0-1%26mode%3Ddesign%26t%3DpzPc1ZJlca6HnPL3-0&sa=D&source=editors&ust=1787257892759133&usg=AOvVaw3vNwnEZa9HCJ_FLRLy3wd-)

Готовое приложение выложить на GitHub / Bitbucket

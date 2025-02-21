[![Python 3.10.10](https://img.shields.io/badge/python-3.10.10-blue.svg)](https://www.python.org/downloads/release/python-31010/)

# На данный момент отбор на стажировку завершен.
## How to run app
1. up DB and broker
```shell
docker compose up -d --build
```
1. install requirements
2. export env variables
```shell
export $(grep -v '^#' .env | xargs)
```
4. Create DB tables and fill_handbooks
```shell
python manage.py alchemy_create api
python manage.py fill_handbooks
```
5. up app
```shell
python manage.py runserver
```
6. up celery
```shell
celery -A core.celery_config worker -l INFO
```
7. Check everything is ok
```shell
curl --location 'http://127.0.0.1:8000/api/auth/auth/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "engine": "email",
    "credentials": {
        "email": "super_admin@example.com",
        "password": "StrongPass777"
    }
}'
```
Example response
```shell
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjQxNzE1YzMtY2UxMi00MTYxLTgwZGEtYmFlYmUwYzU5MGE5IiwiZXhwIjoxNjg1ODIyMjg1fQ.o45cS8Upwz562l5XNmgzaOMz3mZUe0dr8Ea7LnM_lxM",
    "user": {
        "time_created": 1685562975,
        "time_updated": 1685562975,
        "user_id": "241715c3-ce12-4161-80da-baebe0c590a9",
        "user_type": "SUPER_ADMIN",
        "email": "super_admin@example.com",
        "is_email_confirmed": true,
        "last_name": "super",
        "first_name": "admin",
        "is_confirmed": true,
        "is_blocked": false
    }
}
```
## How to run tests
1. install requirements-dev.txt
2. run tests
```shell
pytest tests
```
# Что надо сделать
1. Скачать .zip файл себе данный репозиторий
2. Наполнить тестами на свой вкус (желательно не тратить на это больше 1-2 дней)
3. Прислать ссылку на свой репозиторий
### Приветствуется, но не обязательно:
1. использование параметризации тестов
2. использование моков
3. тесты значений в БД
4. тесты celery таски
5. организовать запуск тестов параллельно (по числу ядер на машине)
6. рефакторинг \ исправление ошибок в коде
# Начало работы
Для проверки работы приложения локально нужно выполнить следующие действия

## Установка проекта

1. Скачивание репозитория
    ```bash
    git clone git@github.com:smenateam/assignments.git
    cd assignments/devops
    ```
   
1. Необходим интерпретатор Python3.9 https://www.python.org/downloads/

1. Создание виртуального окружения и установка зависимостей
    ```bash
    pip install poetry
    poetry install
    ```

## Запуск сервера

1. Запуск сервера
    ```bash
    poetry shell
    (.venv)> make run
    ```

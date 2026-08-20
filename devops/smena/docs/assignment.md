# Тестовое задание DevOps разработчик

Имеется приложение hello-world написанное на Python + FastAPI, которое отдает строку `"Hello World <окружение>!"`.

## Задачи

1. Завести публичный репозиторий на GitHub или аналогах, в который скопировать весь проект из директории `devops` и продолжать работу в нем

2. Завернуть это приложение в Dockerfile, в котором
   1. Установятся зависимости через poetry ([установка через poetry](project_install.md))
   2. Будет запускаться приложение через web-сервер `gunicorn` ([gunicorn.sh](../gunicorn.sh))

3. Написать helm chart. в котором
   1. [Configmap](../deploy/chart/templates/configmap.yaml) для переменных окружения ([ENVIRONMENT](../app/config.py))
      1. Переменная `ENVIRONMENT` должна иметь значения: `dev`, `stage`, `prod` в зависимости от окружения
   2. [Secret](../deploy/chart/templates/secret.yaml) для секретных переменных окружения ([ENVIRONMENT_FROM_SECRET](../app/config.py))
      1. Секреты должны шифроваться любым способом доступным для k8s (например: `helm-secrets`)
      2. Секрет `ENVIRONMENT_FROM_SECRET` должен иметь значения: `secret_dev`, `secret_stage`, `secret_prod` в зависимости от окружения
   3. [Deployment](../deploy/chart/templates/deployment.yaml), который будет 
      1. Запускать 2 реплики приложения
      2. Работать на `8000` порте
      2. Прокидывать в контейнер `ConfigMap` и `Secret`
      3. Иметь readiness и liveness probes по эндпоинту `/healthcheck`
   4. [Service](../deploy/chart/templates/service.yaml) типа ClusterIP
   5. [Ingress](../deploy/chart/templates/ingress.yaml) для nginx сервера, который должен сконфигурирован для хостов
      1. dev - localhost
      2. stage - farforstaging.ru
      3. prod - farfor.ru
   6. [CertManager](../deploy/chart/templates/certmanager.yaml) в котором
      1. `Issuer` для выписывания сертификатов acme-letsencrypt через `http01.ingess`
      2. `Certificate` - соответствующий сертификат связанный с `Issuer` для доменов окружений `stage` и `prod`
      - P.S. Ествественно не нужно пытаться выписывать сертификаты, только написать манифесты
   7. [HorizontalPodAutoscaler](../deploy/chart/templates/hpa.yaml), который будет
      1. Скейлить реплики от 2 до 4
      2. Триггер для скейла будет использование CPU или ОЗУ в 80%
   8. [_helpers.tpl](../deploy/chart/templates/_helpers.tpl), в котором определить шаблоны для
      1. `selectorlabels`, в котором определить селекторные метки `app` и `release`
      2. `labels` включающий в себя `selectorLabels`, в котором определить общие метки `chart` и `version` + `selectorLabels`
      и использовать шаблоны в нужных местах в чарте
   9. [helmfile](../deploy/helmfile.yaml) для трех (`dev`, `stage`, `prod`) окружений
   10. Максимально использовать общие переменные и переиспользовать переменные окружений по необходимости 
   11. Написать полную пошаговую инструкцию по сборке приложения и запуску через minikube

## Итог
Приложение должно:
   1. Собираться через Dockerfile
   2. Запускаться через minikube
   3. Работать по адресу http://0.0.0.0:8000/ и отображать значение переменной `ENVIRONMENT` в ответе
   4. По адресу http://0.0.0.0:8000/docs отображать значение переменной `ENVIRONMENT_FROM_SECRET` в заголовке страницы

Подготовлены файлы конфигураций для всех окружений
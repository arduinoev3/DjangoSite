# DjangoSite

Краткое описание

Проект DjangoSite — веб-приложение на Django, включающее модульную структуру с приложениями `logic` и `appeals`, интеграцией с Telegram-ботом и готовностью к развёртыванию на Heroku.

## Основные функции

- Веб-интерфейс на Django
- Интеграция с Telegram (webhook)
- Приложения: `logic`, `appeals`
- Поддержка Celery/cron задач (зависимости в `requirements.txt`)

## Технологический стек

- Python 3.6
- Django 3.1
- Celery
- PostgreSQL (через dj-database-url при продакшн-конфигурации)
- Gunicorn
- Whitenoise для статических файлов

## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение и активируйте его
3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Выполните миграции:

```bash
python djangoShow/manage.py migrate
```

## Переменные окружения

Проект использует переменные окружения, которые могут быть вынесены в `settings/config.py` в development или заданы в окружении при деплое:

- DJANGO_SETTINGS_MODULE — модуль настроек (по умолчанию `settings.settings`)
- DEBUG — флаг debug (boolean)
- SITE — доменное имя приложения (пример: `example.herokuapp.com`)
- TELEGRAM_TOKEN — токен бота
- DATABASE_URL — URL для postgres (используется `dj-database-url`)

Пример в `djangoShow/settings/config.py` (примерный):

```py
site = '.herokuapp.com'
DEBUG = False
token = '<TELEGRAM_TOKEN>'
MODE = 'WEBHOOK'
```

## Запуск локально

1. Соберите статические файлы:

```bash
python djangoShow/manage.py collectstatic --noinput
```

2. Запустите сервер разработки:

```bash
python djangoShow/manage.py runserver
```

Для продакшн-реконфигурации используется Gunicorn (см. `Procfile`):

```bash
gunicorn djangoShow.wsgi --log-file -
```

## Структура проекта

- `djangoShow/` — корень Django проекта
  - `logic/` — основное приложение с бизнес-логикой
  - `appeals/` — приложение для обращений/жалоб
  - `settings/` — конфигурация проекта
  - `manage.py` — управляющий скрипт
- `requirements.txt` — зависимости
- `Procfile`, `runtime.txt` — прицельная конфигурация для Heroku

## Тесты

Запуск тестов через manage.py:

```bash
python djangoShow/manage.py test
```

## Важные нюансы

- В `djangoShow/settings/config.py` хардкодятся значения `token` и `site`. Для безопасности вынесите настоящие секреты в переменные окружения и не коммитьте их в репозиторий.
- В `requirements.txt` указана старая версия Python (3.6) и некоторые зависимости могут нуждаться в обновлении.
- Проект использует `django_telegrambot` и `python-telegram-bot` — проверьте версии и совместимость.

## Лицензия

Этот проект лицензируется под MIT License — см. файл `LICENSE`.

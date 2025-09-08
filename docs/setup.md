# Установка и локальная настройка

Этот документ описывает шаги для быстрого запуска проекта локально для разработки.

1) Клонирование

	git clone <repo-url>

2) Виртуальное окружение

	python3 -m venv .venv
	source .venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

3) Переменные окружения

Установите переменные окружения, необходимые приложению. Минимум для разработки:

- DJANGO_DEBUG=True
- DJANGO_SECRET_KEY — используйте случайную строку
- TELEGRAM_TOKEN — если используете Telegram интеграцию

Пример для macOS/zsh:

	export DJANGO_DEBUG=True
	export DJANGO_SECRET_KEY="dev-secret"
	export TELEGRAM_TOKEN="your-token"

4) Миграции и создание суперпользователя

	python djangoShow/manage.py migrate
	python djangoShow/manage.py createsuperuser

5) Запуск

	python djangoShow/manage.py runserver

6) Опционально: Celery

Если вы планируете использовать Celery, запустите worker отдельно:

	celery -A djangoShow worker -l info

7) Отладка и логи

Логи Django выводятся в STDOUT при запуске `runserver`. Для продакшена настройте отдельный логгер и хранение логов (например, Sentry).


# Установка и локальный запуск

1. Клонируйте репозиторий и перейдите в корень проекта.

2. Создайте виртуальное окружение (рекомендуется `venv`):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения. Для локальной разработки можно временно отредактировать `djangoShow/settings/config.py`, но рекомендуется использовать `.env` или экспорт переменных в shell:

```bash
export DJANGO_SETTINGS_MODULE=settings.settings
export DEBUG=True
export TELEGRAM_TOKEN="<your-token>"
export SITE="localhost"
```

5. Выполните миграции и соберите статику:

```bash
python djangoShow/manage.py migrate
python djangoShow/manage.py collectstatic --noinput
```

6. Запустите сервер разработки:

```bash
python djangoShow/manage.py runserver
```

7. Запуск тестов:

```bash
python djangoShow/manage.py test
```

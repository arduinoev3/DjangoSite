# Развёртывание (Heroku)

Проект содержит `Procfile` и `runtime.txt` для деплоя на Heroku.

1. Войдите в Heroku и создайте приложение.

2. Установите переменные окружения в Heroku (Settings -> Config Vars):

- `DJANGO_SETTINGS_MODULE` = `settings.settings`
- `DEBUG` = `False`
- `TELEGRAM_TOKEN` = `<your-token>`
- `SITE` = `<your-app>.herokuapp.com`
- `DATABASE_URL` = `<postgres-connection>` (если требуется)

3. Запушьте репозиторий в Heroku git и выполните миграции:

```bash
git push heroku master
heroku run python djangoShow/manage.py migrate
heroku run python djangoShow/manage.py collectstatic --noinput
```

4. Gunicorn будет использоваться как WSGI-сервер (см. `Procfile`).

Примечание: В `djangoShow/settings/config.py` по умолчанию прописаны `site` и `token`. Для безопасности замените их на переменные окружения.

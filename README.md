# DjangoSite

Краткое описание
-----------------

DjangoSite — это веб-приложение на Django (3.1) с набором внутренних приложений: `logic` и `appeals`. Проект включает интеграцию с Telegram-ботом, поддержку фоновых задач (Celery), настройки для развёртывания на Heroku и статической выдачи через WhiteNoise.

Основные возможности
--------------------

- Веб-интерфейс и шаблоны для управления контентом (пакет `logic`).
- Модуль обращений/жалоб (`appeals`).
- Интеграция с Telegram через `django_telegrambot` (WEBHOOK режим).
- Поддержка фоновых задач через Celery и планирования задач (APScheduler).
- Конфигурация, совместимая с Heroku (пакет `django_heroku` и `dj-database-url`).

Стек
-----

- Python 3.8+ (репозиторий использует пакеты, совместимые с Python 3.8)
- Django 3.1
- Celery
- django-telegrambot / python-telegram-bot
- WhiteNoise для статики
- SQLite по умолчанию, но подготовлено для Postgres на Heroku

Быстрый старт (локально)
-----------------------

1. Клонировать репозиторий:

	git clone <repo-url>

2. Создать виртуальное окружение и установить зависимости:

	python3 -m venv .venv
	source .venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

3. Настроить переменные окружения (см. раздел "Переменные окружения").

4. Выполнить миграции и запустить сервер:

	python djangoShow/manage.py migrate
	python djangoShow/manage.py runserver

Установка и окружение
---------------------

Рекомендуется использовать виртуальное окружение и Python 3.8+. Все зависимости перечислены в `requirements.txt`.

Переменные окружения
---------------------

Необходимо задать как минимум следующие переменные в продакшене и/или при локальной разработке, если вы переопределяете значения в `djangoShow/settings/config.py`:

- DJANGO_DEBUG — включить/выключить DEBUG (True/False)
- DJANGO_SECRET_KEY — секретный ключ Django
- DATABASE_URL — строка подключения к базе данных (для Postgres/Heroku)
- TELEGRAM_TOKEN — токен Telegram-бота (если используете бот)
- SITE_DOMAIN — домен сайта (используется для webhook)

Пример (macOS / zsh):

	export DJANGO_DEBUG=False
	export DJANGO_SECRET_KEY="your-secret-key"
	export DATABASE_URL=postgres://user:pass@host:5432/dbname
	export TELEGRAM_TOKEN=123:ABC
	export SITE_DOMAIN=example.com

Запуск Celery (локально)
------------------------

Для фоновых задач и очередей:

	celery -A djangoShow worker -l info

Если используется брокер Redis или RabbitMQ — убедитесь, что переменная BROKER_URL/REDIS_URL установлена и брокер запущен.

Структура проекта
-----------------

Основные директории и файлы:

- `djangoShow/` — корневая Django-папка проекта
  - `manage.py` — менеджер Django
  - `settings/` — настройки проекта (`config.py`, `settings.py` и т.д.)
  - `logic/` — основное приложение с бизнес-логикой
  - `appeals/` — приложение для обращений/жалоб
  - `db.sqlite3` — обычная SQLite БД для разработки
- `requirements.txt` — зависимости
- `Procfile`, `runtime.txt` — файлы для Heroku
- `docs/` — документация (см. ниже)

Тесты
-----

Запуск тестов через Django test runner:

	python djangoShow/manage.py test

Важные нюансы и советы
----------------------

- В `djangoShow/settings/config.py` по умолчанию указан `MODE = 'WEBHOOK'` и примерный `token`. Не храните реальные токены в репозитории; вместо этого используйте переменные окружения.
- `django_heroku.settings(locals())` в `settings.py` автоматически настраивает некоторые параметры для Heroku; проверьте, не переопределяют ли ваши переменные окружения важные настройки.
- По умолчанию проект использует SQLite — для продакшена рекомендуется Postgres (Heroku Postgres).
- WhiteNoise используется для отдачи статических файлов без отдельного CDN в простом деплое.

Лицензия
--------

Проект лицензируется под MIT License — полный текст см. в файле `LICENSE`.
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


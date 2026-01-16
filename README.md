# oreshkiHakatonPython
Хакатон-лабораторная 11

## Авторы:
команда oreshki

Ахметов Артём

Гурьева Евгения

Пак Александра

## Описание
В лабораторной реализовано клиент-сервер приложение на основе фреймворка Django. Оформление выполненно с помощью Bootstrap 5. Реализована миграция, url-роуты, базы данных пользователя и заметок (SQLite, ORM, MVC). Прописаны тесты для основного функционала.

## Запуск
Клонирование репозитория
```
git clone https://github.com/Votemha/oreshkiHakatonPython.git
```
Установка окружения
```
python -m venv venv
```
Установка зависимостей
```
pip install -r requirements.txt
```
Применение миграций
```
python manage.py migrate
```
Запуск сервера разработки
```
python manage.py runserver
```
адрес - http://127.0.0.1:8000/

## Архитектура 
```
oreshkiHakatonPython/
│
├── app/                        # Основное приложение
│   ├── migrations/             # Миграции базы данных
│   │   └── 0001_initial.py
│   │
│   ├── templates/              # HTML
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── user_form.html
│   │   ├── notes_list.html
│   │   └── note_form.html
│   │
│   ├── apps.py
│   ├── models.py               # ORM-модели User и Note
│   ├── tests.py                # Unit-тесты (unittest)
│   ├── urls.py                 # URL-маршруты приложения
│   └── views.py                # Контроллеры (CRUD-логика)
│
├── notes_project/              # Конфигурация проекта
│   ├── asgi.py
│   ├── settings.py             # Настройки Django
│   ├── urls.py                 # Главный URL-роутер
│   └── wsgi.py
│
├── db.sqlite3                  # SQLite база данных
├── manage.py
├── README.md                   # Документация
└── requirements.txt            # Зависимости проекта
```
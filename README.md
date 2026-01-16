# oreshkiHakatonPython
Хакатон-лабораторная 11

## скринкаст
https://drive.google.com/file/d/1bP8Ep203if6TybsMRYIImfLDCHYPCqXY/view?usp=sharing

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

## Работа в группах
Использовалась модель ветвления кода - gitlab flow, были разделены зоны ответственности: Ахметов Артём - система пользователей, Гурьева Евгения - система заметок, Александра Пак - шаблонизация, маршрутизация. Работа с тасками - kanban ![kanban](./source/Снимок%20экрана%202026-01-17%20в%2002.13.43.png)

## Модель
В моделе реализовано обращение через ORM Django к пользователю и заметкам. Можно создавать, получать, удалять записи

## Контроллер
Файл views. Принимает запросы клиента, получает данные из бд, передает их в шаблоны, возвращает клиенту html

## Шаблоны
В папке templates. Получают данные из контроллера, выводят их пользователю

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

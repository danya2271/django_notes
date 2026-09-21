# NoteSpace

Учебный Django-проект по варианту 4: приложение для создания и хранения заметок с разными темами оформления.

## Что реализовано

- HTML-форма для создания заметки: заголовок, текст, категория и приоритет.
- Форма пользовательских настроек: тема, язык интерфейса и размер текста.
- Сохранение пользовательских настроек через cookies.
- Сохранение созданных заметок в подписанный cookie браузера.
- Данные-примеры в коде через списки и словари.
- Внешняя таблица стилей и статическая иллюстрация.
- Тесты Django для главной страницы, cookies и формы заметки.

## Установка и запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

После запуска откройте страницу:

```text
http://127.0.0.1:8000/
```

## Запуск тестов

```bash
source .venv/bin/activate
python manage.py test
```

## Структура проекта

```text
config/                  настройки Django-проекта
notes/                   приложение с заметками
notes/data.py            данные в коде: темы, категории, демо-заметки
notes/forms.py           формы заметки и настроек
notes/templates/         HTML-шаблоны
notes/static/            CSS и графический контент
requirements.txt         зависимости проекта
```

## Публикация на GitHub

Создайте пустой репозиторий на GitHub, затем выполните команды в папке проекта:

```bash
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

Замените `USERNAME` и `REPOSITORY` на свои значения.

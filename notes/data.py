THEMES = {
    "paper": {
        "label": "Бумажная",
        "description": "Светлая тема для дневных заметок.",
    },
    "midnight": {
        "label": "Полночь",
        "description": "Темная тема для вечернего планирования.",
    },
    "sage": {
        "label": "Шалфей",
        "description": "Спокойная зеленая тема для учебы.",
    },
}

LANGUAGES = {
    "ru": "Русский",
    "en": "English",
}

FONT_SIZES = {
    "compact": "Компактный",
    "normal": "Обычный",
    "large": "Крупный",
}

CATEGORIES = {
    "study": "Учеба",
    "personal": "Личное",
    "ideas": "Идеи",
    "tasks": "Задачи",
}

PRIORITIES = {
    "low": "Низкий",
    "normal": "Обычный",
    "high": "Высокий",
}

DEFAULT_NOTES = [
    {
        "id": "demo-1",
        "title": "План на неделю",
        "text": "Подготовить конспект, проверить дедлайны и выбрать одну большую задачу на каждый день.",
        "category": "tasks",
        "priority": "high",
        "created_at": "20.09.2026 18:30",
        "source": "demo",
    },
    {
        "id": "demo-2",
        "title": "Идея для проекта",
        "text": "Добавить быстрые цветовые метки к заметкам, чтобы легче отличать учебу, личные дела и идеи.",
        "category": "ideas",
        "priority": "normal",
        "created_at": "19.09.2026 11:10",
        "source": "demo",
    },
    {
        "id": "demo-3",
        "title": "Список литературы",
        "text": "Сохранить ссылки на материалы по Django, cookies и работе со статическими файлами.",
        "category": "study",
        "priority": "low",
        "created_at": "18.09.2026 09:45",
        "source": "demo",
    },
]

UI_COPY = {
    "ru": {
        "app_name": "NoteSpace",
        "headline": "Заметки с персональными настройками",
        "lead": "Создавайте короткие записи, выбирайте оформление и возвращайтесь к последним настройкам в браузере.",
        "new_note": "Новая заметка",
        "settings": "Настройки интерфейса",
        "save_note": "Сохранить заметку",
        "save_settings": "Сохранить настройки",
        "notes": "Ваши заметки",
        "demo_badge": "пример",
        "saved_badge": "ваша",
        "last_page": "Последняя страница",
        "last_visit": "Последний визит",
        "empty_cookie": "пока нет данных",
        "theme": "Тема",
        "language": "Язык",
        "font_size": "Размер текста",
    },
    "en": {
        "app_name": "NoteSpace",
        "headline": "Notes with personal preferences",
        "lead": "Write short notes, choose the interface style, and keep your latest browser settings.",
        "new_note": "New note",
        "settings": "Interface settings",
        "save_note": "Save note",
        "save_settings": "Save settings",
        "notes": "Your notes",
        "demo_badge": "sample",
        "saved_badge": "yours",
        "last_page": "Last page",
        "last_visit": "Last visit",
        "empty_cookie": "no data yet",
        "theme": "Theme",
        "language": "Language",
        "font_size": "Text size",
    },
}

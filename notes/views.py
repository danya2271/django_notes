import json

from django.core.signing import BadSignature
from django.shortcuts import redirect, render
from django.utils import timezone

from .data import (
    CATEGORIES,
    DEFAULT_NOTES,
    FONT_SIZES,
    LANGUAGES,
    PRIORITIES,
    THEMES,
    UI_COPY,
)
from .forms import NoteForm, PreferencesForm


PREFERENCES_MAX_AGE = 60 * 60 * 24 * 90
NOTES_MAX_AGE = 60 * 60 * 24 * 30
NOTES_COOKIE = "notespace_notes"
NOTES_COOKIE_SALT = "notespace.notes"


def _clean_cookie_value(request, name, allowed_values, default):
    value = request.COOKIES.get(name, default)
    if value not in allowed_values:
        return default
    return value


def _read_preferences(request):
    return {
        "theme": _clean_cookie_value(request, "theme", THEMES, "paper"),
        "language": _clean_cookie_value(request, "language", LANGUAGES, "ru"),
        "font_size": _clean_cookie_value(request, "font_size", FONT_SIZES, "normal"),
    }


def _read_user_notes(request):
    try:
        raw_notes = request.get_signed_cookie(
            NOTES_COOKIE,
            default="[]",
            salt=NOTES_COOKIE_SALT,
        )
    except BadSignature:
        return []

    try:
        notes = json.loads(raw_notes)
    except json.JSONDecodeError:
        return []

    if not isinstance(notes, list):
        return []

    return [note for note in notes if isinstance(note, dict)]


def _decorate_notes(notes):
    decorated = []
    for note in notes:
        decorated.append(
            {
                **note,
                "category_label": CATEGORIES.get(note.get("category"), "Без категории"),
                "priority_label": PRIORITIES.get(note.get("priority"), "Обычный"),
            }
        )
    return decorated


def _remember_visit(response, request):
    now = timezone.localtime().strftime("%d.%m.%Y %H:%M")
    response.set_cookie("last_page", request.path, max_age=PREFERENCES_MAX_AGE, samesite="Lax")
    response.set_cookie("last_visit", now, max_age=PREFERENCES_MAX_AGE, samesite="Lax")


def _apply_preferences(response, preferences):
    for name, value in preferences.items():
        response.set_cookie(name, value, max_age=PREFERENCES_MAX_AGE, samesite="Lax")


def _save_user_notes(response, notes):
    response.set_signed_cookie(
        NOTES_COOKIE,
        json.dumps(notes[:8]),
        salt=NOTES_COOKIE_SALT,
        max_age=NOTES_MAX_AGE,
        httponly=True,
        samesite="Lax",
    )


def home(request):
    preferences = _read_preferences(request)
    user_notes = _read_user_notes(request)
    note_form = NoteForm()
    preferences_form = PreferencesForm(initial=preferences)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "note":
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                cleaned_note = note_form.cleaned_data
                user_notes.insert(
                    0,
                    {
                        "id": f"user-{int(timezone.now().timestamp())}",
                        "title": cleaned_note["title"],
                        "text": cleaned_note["text"],
                        "category": cleaned_note["category"],
                        "priority": cleaned_note["priority"],
                        "created_at": timezone.localtime().strftime("%d.%m.%Y %H:%M"),
                        "source": "user",
                    },
                )
                response = redirect("notes:home")
                _save_user_notes(response, user_notes)
                _remember_visit(response, request)
                return response

        if action == "preferences":
            preferences_form = PreferencesForm(request.POST)
            if preferences_form.is_valid():
                response = redirect("notes:home")
                _apply_preferences(response, preferences_form.cleaned_data)
                _remember_visit(response, request)
                return response

    copy = UI_COPY.get(preferences["language"], UI_COPY["ru"])
    notes = _decorate_notes(user_notes + DEFAULT_NOTES)
    context = {
        "copy": copy,
        "note_form": note_form,
        "preferences": preferences,
        "preferences_form": preferences_form,
        "themes": THEMES,
        "notes": notes,
        "last_page": request.COOKIES.get("last_page"),
        "last_visit": request.COOKIES.get("last_visit"),
    }
    response = render(request, "notes/home.html", context)
    _remember_visit(response, request)
    return response

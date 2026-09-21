from django import forms

from .data import CATEGORIES, FONT_SIZES, LANGUAGES, PRIORITIES, THEMES


class NoteForm(forms.Form):
    title = forms.CharField(
        label="Заголовок",
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Например: подготовка к занятию",
                "class": "field-control",
            }
        ),
    )
    text = forms.CharField(
        label="Текст заметки",
        max_length=600,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Коротко запишите мысль, задачу или идею",
                "rows": 5,
                "class": "field-control",
            }
        ),
    )
    category = forms.ChoiceField(
        label="Категория",
        choices=[(key, value) for key, value in CATEGORIES.items()],
        widget=forms.Select(attrs={"class": "field-control"}),
    )
    priority = forms.ChoiceField(
        label="Приоритет",
        choices=[(key, value) for key, value in PRIORITIES.items()],
        initial="normal",
        widget=forms.RadioSelect(attrs={"class": "choice-list"}),
    )


class PreferencesForm(forms.Form):
    theme = forms.ChoiceField(
        label="Тема",
        choices=[(key, value["label"]) for key, value in THEMES.items()],
        widget=forms.RadioSelect(attrs={"class": "choice-list"}),
    )
    language = forms.ChoiceField(
        label="Язык",
        choices=[(key, value) for key, value in LANGUAGES.items()],
        widget=forms.Select(attrs={"class": "field-control"}),
    )
    font_size = forms.ChoiceField(
        label="Размер текста",
        choices=[(key, value) for key, value in FONT_SIZES.items()],
        widget=forms.Select(attrs={"class": "field-control"}),
    )

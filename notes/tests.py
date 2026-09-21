from django.test import TestCase
from django.urls import reverse

from .views import NOTES_COOKIE


class NotesHomeViewTests(TestCase):
    def test_home_page_renders_and_sets_visit_cookies(self):
        response = self.client.get(reverse("notes:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "NoteSpace")
        self.assertContains(response, "План на неделю")
        self.assertIn("last_page", response.cookies)
        self.assertIn("last_visit", response.cookies)
        self.assertEqual(response.cookies["last_page"].value, "/")

    def test_preferences_are_saved_to_cookies(self):
        response = self.client.post(
            reverse("notes:home"),
            {
                "action": "preferences",
                "theme": "midnight",
                "language": "en",
                "font_size": "large",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.cookies["theme"].value, "midnight")
        self.assertEqual(response.cookies["language"].value, "en")
        self.assertEqual(response.cookies["font_size"].value, "large")

    def test_note_form_saves_note_to_signed_cookie(self):
        response = self.client.post(
            reverse("notes:home"),
            {
                "action": "note",
                "title": "Контрольная заметка",
                "text": "Проверить сохранение заметки через cookie.",
                "category": "study",
                "priority": "high",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn(NOTES_COOKIE, response.cookies)

        response = self.client.get(reverse("notes:home"))

        self.assertContains(response, "Контрольная заметка")
        self.assertContains(response, "Проверить сохранение заметки через cookie.")

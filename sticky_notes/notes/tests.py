from django.test import TestCase
from django.urls import reverse

from .models import Author, Note


class NoteModelTest(TestCase):

    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name="Test Author")

        # Create a Note object for testing
        Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=author
        )

    def test_note_has_title(self):
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note.")


class NoteCreateTest(TestCase):

    def setUp(self):
        # Create an Author object
        self.author = Author.objects.create(name="Test Author")

    def test_create_note(self):
        # Submit the create form
        response = self.client.post(
            reverse("note_create"),
            {
                "title": "New Note",
                "content": "This is a new note.",
                "author": self.author.id
            }
        )

        # Check that the user is redirected after creating the note
        self.assertEqual(response.status_code, 302)

        # Check that the Note was created
        self.assertEqual(Note.objects.count(), 1)

        note = Note.objects.first()
        self.assertEqual(note.title, "New Note")
        self.assertEqual(note.content, "This is a new note.")

    def test_create_note_invalid_form(self):
        # Submit an empty form
        response = self.client.post(
            reverse("note_create"),
            {
                "title": "",
                "content": ""
            }
        )

        # Check that the form is rejected
        self.assertEqual(response.status_code, 200)

        # Check that no Note was created
        self.assertEqual(Note.objects.count(), 0)


class NoteUpdateTest(TestCase):

    def setUp(self):
        # Create an Author object
        self.author = Author.objects.create(name="Test Author")

        # Create a Note object
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=self.author
        )

    def test_update_note(self):
        # Submit the edit form
        response = self.client.post(
            reverse("note_update", args=[self.note.id]),
            {
                "title": "Updated Note",
                "content": "This note has been updated.",
                "author": self.author.id
            }
        )

        # Check that the user is redirected
        self.assertEqual(response.status_code, 302)

        # Get the updated Note
        self.note.refresh_from_db()

        # Check that the Note was updated
        self.assertEqual(self.note.title, "Updated Note")
        self.assertEqual(
            self.note.content,
            "This note has been updated."
        )

    def test_update_missing_note(self):
        # Try to update a Note that does not exist
        response = self.client.get(
            reverse("note_update", args=[9999])
        )

        # Check for a 404 response
        self.assertEqual(response.status_code, 404)


class NoteDeleteTest(TestCase):

    def setUp(self):
        # Create an Author object
        self.author = Author.objects.create(name="Test Author")

        # Create a Note object
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=self.author
        )

    def test_delete_note(self):
        # Submit the delete request
        response = self.client.post(
            reverse("note_delete", args=[self.note.id])
        )

        # Check that the user is redirected
        self.assertEqual(response.status_code, 302)

        # Check that the Note was deleted
        self.assertEqual(Note.objects.count(), 0)

    def test_delete_missing_note(self):
        # Try to delete a Note that does not exist
        response = self.client.post(
            reverse("note_delete", args=[9999])
        )

        # Check for a 404 response
        self.assertEqual(response.status_code, 404)
from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note objects.

    Fields:
    - title: CharField for the note title.
    - content: TextField for the note content.
    - author: ForeignKey for the author of the note.

    Meta class:
    - Defines the model to use (Note) and the fields to include
      in the form.
    """

    class Meta:
        model = Note
        fields = ["title", "content", "author"]

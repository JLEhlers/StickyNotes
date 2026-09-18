from django.contrib import admin

from .models import Author, Note

# Register your models here.
# Note model
admin.site.register(Note)
# Author model
admin.site.register(Author)

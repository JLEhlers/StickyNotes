from django.contrib import admin
from django.urls import include, path

# Define URL patterns for the entire project
urlpatterns = [
    # Admin URL pattern, mapping to the Django admin interface
    path("admin/", admin.site.urls),

    # Include URL patterns from the 'notes' app
    path("", include("notes.urls")),
]

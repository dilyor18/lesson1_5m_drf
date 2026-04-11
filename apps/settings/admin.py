from django.contrib import admin
from .models import About, Contact

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = ("id", "title")
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = ("id", "title")
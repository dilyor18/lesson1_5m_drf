from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "is_active")
    list_display_links = ("id", "email")

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone_number", "address")
    list_display_links = ("id", "user")
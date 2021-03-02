"""User admin classes."""

# Django
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# # Models
# from django.contrib.auth.models import User
from app.models import Profile, Process

class ProfileAdmin(admin.ModelAdmin):

    list_display=("email", "floors", "address")
    search_fields=("email", "address")
    list_filter=("date",)
    date_hierarchy="date"

admin.site.register(Process, ProfileAdmin)

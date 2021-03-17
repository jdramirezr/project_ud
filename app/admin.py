"""User admin classes."""

# Django
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from django.contrib.auth.models import User
from app.models import Profile, Process, AisModel

class ProcessAdmin(admin.ModelAdmin):

    list_display=("email", "floors", "address")
    search_fields=("email", "address")
    list_filter=("date",)
    date_hierarchy="date"


class AisModelAdmin(admin.ModelAdmin):

    list_display=("pk", "option_detail", "option_mooring")

class ProfileAdmin(admin.ModelAdmin):

    list_display=("pk", "user", "date")
    search_fields=("user",)
    list_filter=("date",)



admin.site.register(Process, ProcessAdmin)
admin.site.register(AisModel, AisModelAdmin)
admin.site.register(Profile, ProfileAdmin)
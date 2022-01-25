from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile


class ProfileAdmin(UserAdmin):
    model = Profile
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']


admin.site.register(Profile, ProfileAdmin)

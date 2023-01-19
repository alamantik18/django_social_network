from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff', 'last_login')

admin.site.unregister(Group)
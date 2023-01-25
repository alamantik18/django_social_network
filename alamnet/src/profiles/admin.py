from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User, UserTechnology

@admin.register(User)
class UserCustomAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'technologies')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'middle_name', 'phone', 'email', 'gender', 'birthday')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'first_name', 'email', 'phone', 'is_active', 'is_staff', 'last_login')
    list_filter = ('is_active', 'is_staff', 'last_login')
    search_fields = ('username', 'email', 'phone')

@admin.register(UserTechnology)
class UserTechnologyCustomAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

admin.site.unregister(Group)
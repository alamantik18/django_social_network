from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_date', 'published', 'view_count', 'id')
    # actions = ('unpublish', 'publish')

@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'post', 'created_date', 'updated_date', 'published', 'id')
    # actions = ('unpublish', 'publish')
    mptt_level_indent = 15
from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'excerpt', 'slide_link')
    fields = ['title', 'excerpt', 'body', 'author', 'image', 'slide_link']
    list_filter = ('created_on', 'author')
    search_fields = ('title', 'body', 'author__username', 'author__first_name', 'author__last_name')


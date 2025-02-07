from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post


class PostAdmin(MarkdownxModelAdmin):  
   list_display = ('title', 'slug', 'created_on')
   search_fields = ['title', 'content']
   prepopulated_fields = {'slug': ('title',)}
   fields = ('title', 'slug', 'content', 'banner_image')

admin.site.register(Post, PostAdmin)
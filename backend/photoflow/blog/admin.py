from django.contrib import admin
from .models import Blog
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
class BlogAdmin(MarkdownModelAdmin):
    list_display = ('title','cutted_content','create_time','pinned')
    list_filter = ('create_time','pinned')
    search_fields = ('title',)

    def cutted_content(self,obj):
        return obj.content[:50]


admin.site.register(Blog,BlogAdmin)
from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('id', 'title', 'created_at', 'updated_at', 'author', 'tag', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'tag')
    list_editable = ('is_published', 'tag')
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

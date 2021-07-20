from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from .models import Blog, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {'url': ('title',)}
    list_display = ('id', 'title', 'created_at', 'updated_at', 'author', 'tag', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'tag')
    list_editable = ('is_published', 'tag')
    list_filter = ('is_published', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

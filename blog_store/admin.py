from django.contrib import admin
from .models import Blog


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Blog, PostAdmin)

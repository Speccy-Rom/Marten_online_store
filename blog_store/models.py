from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Blog(models.Model):
    title = models.CharField(max_length=150)
    url = models.SlugField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = TaggableManager()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

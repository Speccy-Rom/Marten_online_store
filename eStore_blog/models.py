from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from taggit.managers import TaggableManager


class Blog(models.Model):
    title = models.CharField(max_length=150)
    url = models.SlugField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')
    tag = TaggableManager()
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse_lazy('view_post', kwargs={'blog_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назваие категории')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['title']

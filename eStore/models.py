import json

from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils import timezone
from taggit.managers import TaggableManager

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['name']

    @property
    def products(self):
        return json.dumps(Product.objects.filter(category=self).values())


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название бренда / марки")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = "Бренды"
        ordering = ['name']

    @property
    def products(self):
        return json.dumps(Product.objects.filter(brand=self).values())


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд/Марка>")
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование продукта')
    slug = models.SlugField(db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Фото товара')
    description = RichTextUploadingField(verbose_name='Описание', null=True)
    tag = TaggableManager(verbose_name='Тэг')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Наличие")
    available = models.BooleanField(default=True, verbose_name='Товар включен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title



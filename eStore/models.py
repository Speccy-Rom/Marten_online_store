import json

from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils import timezone
from taggit.managers import TaggableManager

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    description = RichTextUploadingField(verbose_name='Описание', null=True)
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
    description = RichTextUploadingField(verbose_name='Описание', null=True)
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


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField(default=0, verbose_name="Значение")

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ['-value']


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField(verbose_name='Электронный адрес')
    name = models.CharField("Имя", max_length=100, verbose_name='Имя')
    description = RichTextUploadingField(verbose_name='Описание', null=True)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт", related_name='reviews')

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



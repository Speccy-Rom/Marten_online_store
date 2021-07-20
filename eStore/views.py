from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, DetailView

from .models import *


class ProductsList(ListView):
    model = Product
    # template_name = 'eStore/product_list.html'
    context_object_name = 'products'
    # extra_context = {'title': 'Каталог продуктов'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        context['title'] = 'Каталог продуктов'
        return context

    def get_queryset(self):
        return Product.objects.filter(brand__name="Бренд-1")


class ProductDetail(DetailView):
    model = Product
    # template_name = 'eStore/product_detail.html'
    context_object_name = 'product'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['title'] = Product.objects.get(slug__iexact=self.kwargs['slug'])

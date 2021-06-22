from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Blog


def index(request):
    context = {}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def all_blogs(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs

    html_template = loader.get_template('blog_store/blog.html')
    return HttpResponse(html_template.render(context, request))


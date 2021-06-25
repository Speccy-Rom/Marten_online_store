from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views import View
from taggit.models import Tag

from .models import Blog, Category


def index(request):
    context = {}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def all_blogs(request):
    context = {}
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context['blogs'] = blogs
    context['categories'] = categories

    html_template = loader.get_template('blog_store/blog-leftsidebar.html')
    return HttpResponse(html_template.render(context, request))


def get_category(request, category_id):
    context = {}
    blogs = Blog.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context['blogs'] = blogs
    context['categories'] = categories
    context['category'] = category

    html_template = loader.get_template('blog_store/blog_category.html')
    return HttpResponse(html_template.render(context, request))


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        blog = Blog.objects.filter(tag=tag)
        common_tags = Blog.tag.most_common()
        return render(request, 'blog_store/tag.html', context={
            'title': f'#ТЕГ {tag}',
            'blog': blog,
            'common_tags': common_tags
        })

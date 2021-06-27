from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views import View
from taggit.models import Tag
from django.views.generic import ListView

from .models import Blog, Category


class IndexBlog(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'




# def index(request):
#     context = {}
#
#     html_template = loader.get_template('index.html')
#     return HttpResponse(html_template.render(context, request))


def all_blogs(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs

    html_template = loader.get_template('eStore_blog/blog-leftsidebar.html')
    return HttpResponse(html_template.render(context, request))


def get_category(request, category_id):
    context = {}
    blogs = Blog.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context['blogs'] = blogs
    context['category'] = category

    html_template = loader.get_template('eStore_blog/blog_category.html')
    return HttpResponse(html_template.render(context, request))


def view_post(request, blog_id):
    context = {}
    new_post = get_object_or_404(Blog, pk=blog_id)
    context['new_post'] = new_post
    html_template = loader.get_template('eStore_blog/blog-details.html')
    return HttpResponse(html_template.render(context, request))


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        blog = Blog.objects.filter(tag=tag)
        common_tags = Blog.tag.most_common()
        return render(request, 'eStore_blog/tag.html', context={
            'title': f'#ТЕГ {tag}',
            'blog': blog,
            'common_tags': common_tags
        })

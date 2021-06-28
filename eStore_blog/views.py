from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views import View
from taggit.models import Tag
from django.views.generic import ListView, DeleteView

from .models import Blog, Category


def index_view(request):
    return render(request, 'index.html', {})


class IndexBlog(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'
    extra_context = {'title': 'Home'}  # используем для статических данных, для динамических данных используем

    # переопределение данных через функцию get_context_data


class ListBlog(ListView):
    model = Blog
    template_name = 'eStore_blog/blog-leftsidebar.html'
    context_object_name = 'blogs'
    extra_context = {'title': 'BLOG'}

    def get_context_data(self, *, object_list=None, **kwargs):  # переопределение данных через функцию get_context_data
        context = super(ListBlog, self).get_context_data(**kwargs)
        context['title'] = "Home"
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)  # вносим правки по выборке данных (дополнительное условие)


class BlogByCategory(ListView):
    model = Blog
    template_name = 'eStore_blog/blog_category.html'
    context_object_name = 'blogs'
    allow_empty = False  # отображает 404 код ошибки когда нет объекта как в get_object_or_404

    def get_context_data(self, *, object_list=None, **kwargs):  # переопределение данных через функцию get_context_data
        context = super(BlogByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewPost(DeleteView):
    model = Blog
    template_name = 'eStore_blog/blog-details.html'
    # pk_url_kwarg = 'blog_id'
    context_object_name = 'new_post'


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

# def index(request):
#     context = {}
#
#     html_template = loader.get_template('eStore_blog/home.html')
#     return HttpResponse(html_template.render(context, request))

# def all_blogs(request):
#     context = {}
#     blogs = Blog.objects.all()
#     context['blogs'] = blogs
#
#     html_template = loader.get_template('eStore_blog/blog-leftsidebar.html')
#     return HttpResponse(html_template.render(context, request))


# def get_category(request, category_id):
#     context = {}
#     blogs = Blog.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context['blogs'] = blogs
#     context['category'] = category
#
#     html_template = loader.get_template('eStore_blog/blog_category.html')
#     return HttpResponse(html_template.render(context, request))


# def view_post(request, blog_id):
#     context = {}
#     new_post = get_object_or_404(Blog, pk=blog_id)
#     context['new_post'] = new_post
#     html_template = loader.get_template('eStore_blog/blog-details.html')
#     return HttpResponse(html_template.render(context, request))

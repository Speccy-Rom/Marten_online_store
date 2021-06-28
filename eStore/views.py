from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def all_cats(request):
    context = {}

    html_template = loader.get_template('eStore_core/templates/home.html')
    return HttpResponse(html_template.render(context, request))

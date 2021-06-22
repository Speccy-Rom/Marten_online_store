from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def all_fishs(request):
    context = {}

    html_template = loader.get_template('core/templates/index.html')
    return HttpResponse(html_template.render(context, request))

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('core/base.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('core/home.html')
    return HttpResponse(template.render())

def products(request):
    template = loader.get_template('core/products.html')
    return HttpResponse(template.render())
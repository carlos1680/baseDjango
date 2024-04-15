from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    template = loader.get_template('core/base.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('core/home.html')
    return HttpResponse(template.render())

@login_required
def products(request):
    return render(request, 'core/products.html')

def exit(request):
    logout(request)
    return redirect('home')
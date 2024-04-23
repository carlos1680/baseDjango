from django.shortcuts import render
# Create your views here.

def login(request):
    template = loader.get_template('usuarios/login.html')
    return HttpResponse(template.render())
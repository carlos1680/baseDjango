from django.shortcuts import render
# Create your views here.

def login(request):
    template = loader.get_template('registration/login.html')
    return HttpResponse(template.render())
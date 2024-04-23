from django.urls import path
from .views import index, home, dashboard,exit

urlpatterns = [
    #path('testbasico',index,name="index"),
    path('index/',index,name="index"),
    path('dashboard/',dashboard,name="dashboard"),
    path('',home,name="home"),
    path('exit/',exit,name="exit"),

    
]

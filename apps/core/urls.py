from django.urls import path
from .views import index, home, products,exit

urlpatterns = [
    #path('testbasico',index,name="index"),
    path('index/',index,name="index"),
    path('products/',products,name="products"),
    path('',home,name="home"),
    path('exit/',exit,name="exit"),

    
]

from django.urls import path
from .views import index, home,products

urlpatterns = [
    #path('testbasico',index,name="index"),
    path('index',index,name="index"),
    path('products',products,name="products"),
    path('home',home,name="home"),
]

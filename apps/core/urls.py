from django.urls import path
from .views import index

urlpatterns = [
    #path('testbasico',index,name="index"),
    path('',index,name="index"),
]

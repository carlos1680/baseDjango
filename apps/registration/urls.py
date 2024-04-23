from django.urls import path
from .views import login

urlpatterns = [
    # path('testbasico',index,name="index"),
    path('login/', login, name="login"),
    
]

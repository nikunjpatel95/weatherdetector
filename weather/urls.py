from django.urls import path  ##importing path will allow us to specify different urls
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    ## name is just the name given to this specific url,
    ## whenever we want to request or go to the URL, we use this name
    
]
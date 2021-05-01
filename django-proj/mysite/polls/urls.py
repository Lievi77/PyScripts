from django.urls import path

from . import views

#next define the urls that you want to include
urlpatterns = [
    path('', views.index, name='index'),
]
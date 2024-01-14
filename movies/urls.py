from django.urls import path
from . import views

# '' represents root of this app ie 'movies/'
urlpatterns = [
    path('', views.index, name='index')
]
from django.urls import path
from . import views

# '' represents root of this app ie 'movies/'
# /movies/1
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
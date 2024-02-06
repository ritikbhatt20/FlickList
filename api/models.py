from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here. In apis, we refer to the models as resources
class MovieResource(ModelResource):  #it represents the concept of a Movie in a restful api
    class Meta:  # tastypie looks for this inner class Meta
        queryset = Movie.objects.all()
        resource_name = 'movies'
    

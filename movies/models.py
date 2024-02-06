from django.db import models
from django.utils import timezone

# Create your models here. models are python class that we use to represent data
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    # Genre(object 1) defalut string representation, to change that 
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=255)        
    release_year = models.IntegerField()                  
    number_in_stock = models.IntegerField()               
    daily_rate = models.FloatField()                     
    # now we need to pass an attribute to movie which is connected to a genre 
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) #what will happen when we delete a genre, CASCADE means all movies associated with that genre will be deleted
    date_created = models.DateTimeField(default=timezone.now)
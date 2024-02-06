from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
# all our view fn should take parameter request which means http request , index represents main page of our app
def index(request):
    movies = Movie.objects.all() 
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1) to get a single object
    output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', { 'movies': movies})

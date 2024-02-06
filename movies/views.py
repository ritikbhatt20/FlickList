from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
# all our view fn should take parameter request which means http request , index represents main page of our app


def index(request):
    movies = Movie.objects.all()
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1) to get a single object
    output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # try:
        # we can also use pk instead of id
        # movie = Movie.objects.get(id=movie_id)
        # return HttpResponse(movie_id)
        # return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
        # raise Http404()
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

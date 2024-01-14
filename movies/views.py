from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# all our view fn should take parameter request which means http request , index represents main page of our app
def index(request):
    return HttpResponse("Hello World")
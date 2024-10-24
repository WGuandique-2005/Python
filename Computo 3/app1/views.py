from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): 
    return HttpResponse('<a href="/home/">Mi primera pagina con Django</a>')

def  home(request):
    return render(request, 'home.html')
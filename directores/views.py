from django.shortcuts import render

# Create your views here.
from .models import Genre, Pelicula, Director


def index(request):
    peliculas = Pelicula.objects.all()
    
    
    return render(request,
                  'index.html',
                  context={
                      'peliculas':peliculas,
                      
                  }
    )

from django.db import models

# Create your models here.
from uuid import uuid4
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Pelicula(models.Model):
    name =models.CharField(max_length=200, help_text='Nombre de la pelicula')
    description = models.TextField(max_length=200, help_text='descripcion de la pelicula')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.name
     
  


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    def __str__(self) :
        return '%s (%s)' % (self.last_name, self.first_name)
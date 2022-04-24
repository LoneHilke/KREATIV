from email.mime import image
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

class Meetup(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    description =models.TextField(max_length=200)
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    #address = models.

    def __str__(self):
        return f'{self.title} - {self.slug}'


    

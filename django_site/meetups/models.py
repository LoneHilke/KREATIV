from email.mime import image
from django.db import models

# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    description =models.TextField(max_length=200)
    #location =models.
    #address = models.
    #image = models.

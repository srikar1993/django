from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=30)
    release_date = models.DateField()
    hero = models.CharField(max_length=30)
    heroin = models.CharField(max_length=30)

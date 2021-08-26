from django.db import models

# Create your models here.

class Cricket(models.Model):
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    victory = models.CharField(max_length=30)

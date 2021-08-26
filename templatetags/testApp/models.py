from django.db import models

# Create your models here.

class Sports(models.Model):
    name = models.CharField(max_length=30)
    players = models.IntegerField()

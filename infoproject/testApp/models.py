from django.db import models

# Create your models here.

class Information(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name
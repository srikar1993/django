from django.db import models
from django.urls import reverse

# Create your models here.

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ebonus')

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    ebonus = models.FloatField()
    ecity = models.CharField(max_length=64)
    objects = CustomManager()

    def get_absolute_url(self):
        return reverse("single", kwargs={"pk": self.pk})


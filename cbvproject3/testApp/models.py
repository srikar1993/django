from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)

    def get_absolute_url(self):
        # return reverse('single', kwargs={'pk': self.pk})
        return reverse('retrieve')
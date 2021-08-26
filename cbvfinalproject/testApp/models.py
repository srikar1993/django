from django.db import models
from django.urls import reverse

# Create your models here.

class Innovation(models.Model):
    innovation = models.CharField(max_length=200)
    innovator = models.CharField(max_length=200)
    year = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('single', kwargs={'pk': self.pk})


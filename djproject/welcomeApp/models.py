from django.db import models

# Create your models here.

class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    def __str__(self):
        return self.job_title, self.qualification
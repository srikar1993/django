from django.db import models

# Create your models here.

class Employee(models.Model):
    empNo = models.IntegerField()
    empName = models.CharField(max_length=30)
    empSal = models.FloatField()
    empAddr = models.CharField(max_length=30)
    def __str__(self):
        return self.empName
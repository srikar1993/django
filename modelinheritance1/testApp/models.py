from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    class Meta:
        abstract = True

class Student(ContactInfo):
    rollNo = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()
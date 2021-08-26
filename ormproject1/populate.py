import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormproject1.settings')
import django
django.setup()

from testApp.models import Employee
from faker import Faker
from random import *

faker = Faker()

def populate(n):
    for i in range(n):
        feno = randint(1001, 9999)
        fename = faker.name()
        fesal = randint(15000, 30000)
        febonus = randint(2000, 5000)
        fecity = faker.city()
        emp_record = Employee.objects.get_or_create(eno = feno, ename = fename, esal = fesal, ebonus=febonus, ecity = fecity)

populate(30)
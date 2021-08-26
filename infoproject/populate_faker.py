import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infoproject.settings')

import django
django.setup()

from testApp.models  import Information
from faker import Faker
from random import *

fake = Faker()

def phone_number():
    d1 = randint(6,9)
    num = d1
    for i in range(9):
        num *= 10 + i
        if len(str(num)) == 9:
            break
    return num

def populate(n):
    for i in range(n):
        info_name = fake.name()
        info_email = fake.email()
        info_phone = phone_number()
        info_address = fake.address()
        info_record = Information.objects.get_or_create(name=info_name, email=info_email, phone=info_phone, address=info_address)

populate(30)
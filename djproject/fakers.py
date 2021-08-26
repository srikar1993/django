import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproject.settings')
import django
django.setup()

from welcomeApp.models  import HydJobs
from faker import Faker
from random import *

fake = Faker()

def populate(n):
    for i in range(n):
        jdate = fake.date()
        jcompany = fake.company()
        jjob_title = fake.random_element(elements=('Project Manager', 'TeamLead', 'Software Engineer'))
        jqualification = fake.random_element(elements=('B.Sc.', 'M.Sc.', 'B.Tech', 'M.Tech', 'B.A.', 'M.A.'))
        jobsInfo = HydJobs.objects.get_or_create(date=jdate, company = jcompany, job_title = jjob_title, qualification = jqualification)

populate(30)
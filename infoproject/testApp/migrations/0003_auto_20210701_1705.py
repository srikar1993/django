# Generated by Django 2.2 on 2021-07-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_auto_20210701_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

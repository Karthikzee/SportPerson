# Generated by Django 2.2.8 on 2019-12-18 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191218_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 18, 21, 58, 6, 909783), verbose_name='date published'),
        ),
    ]

# Generated by Django 2.2.8 on 2019-12-18 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191218_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_content', models.TextField()),
                ('job_published', models.DateTimeField(default=datetime.datetime(2019, 12, 18, 23, 15, 31, 868600), verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]

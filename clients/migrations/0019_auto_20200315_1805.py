# Generated by Django 3.0.3 on 2020-03-15 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_auto_20200315_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 18, 5, 3, 955875)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 18, 5, 3, 955853)),
        ),
    ]

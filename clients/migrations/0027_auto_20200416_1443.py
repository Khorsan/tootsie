# Generated by Django 3.0.3 on 2020-04-16 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0026_auto_20200416_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 14, 43, 7, 446196)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 14, 43, 7, 446173)),
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-16 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0025_auto_20200416_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 14, 42, 4, 844012)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 14, 42, 4, 843990)),
        ),
    ]
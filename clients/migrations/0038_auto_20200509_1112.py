# Generated by Django 3.0.3 on 2020-05-09 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0037_auto_20200508_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-15 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20200315_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 16, 42, 10, 607731)),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 16, 42, 10, 607709)),
        ),
    ]
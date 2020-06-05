# Generated by Django 3.0.3 on 2020-03-15 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_auto_20200315_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 16, 51, 2, 904813)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 16, 51, 2, 904790)),
        ),
    ]

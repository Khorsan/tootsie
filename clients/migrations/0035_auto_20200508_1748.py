# Generated by Django 3.0.3 on 2020-05-08 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0034_auto_20200508_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 17, 48, 3, 768340)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 17, 48, 3, 768311, tzinfo=utc)),
        ),
    ]

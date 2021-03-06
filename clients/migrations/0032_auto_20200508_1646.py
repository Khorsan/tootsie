# Generated by Django 3.0.3 on 2020-05-08 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0031_auto_20200508_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 16, 46, 57, 613225)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 16, 46, 57, 613200, tzinfo=utc)),
        ),
    ]

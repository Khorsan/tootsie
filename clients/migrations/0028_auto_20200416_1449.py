# Generated by Django 3.0.3 on 2020-04-16 14:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0027_auto_20200416_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 14, 49, 7, 928142)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 14, 49, 7, 928117, tzinfo=utc)),
        ),
    ]

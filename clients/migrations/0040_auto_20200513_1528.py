# Generated by Django 3.0.3 on 2020-05-13 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0039_auto_20200511_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='desconto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='divida',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', 'male'), ('2', 'female')], max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='saldo',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 15, 28, 5, 603346)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 15, 28, 5, 603325)),
        ),
    ]

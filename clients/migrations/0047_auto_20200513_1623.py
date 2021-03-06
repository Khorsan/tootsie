# Generated by Django 3.0.3 on 2020-05-13 16:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0046_auto_20200513_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='teste',
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 16, 23, 35, 724058)),
        ),
        migrations.AlterField(
            model_name='event',
            name='instructor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clients.Instructor'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 16, 23, 35, 724035)),
        ),
        migrations.AlterField(
            model_name='session',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Instructor'),
        ),
    ]

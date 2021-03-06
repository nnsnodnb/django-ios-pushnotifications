# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_certfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='certfile',
            name='filename',
            field=models.CharField(default='cert.pem', max_length=100),
        ),
        migrations.AddField(
            model_name='certfile',
            name='is_use',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='certfile',
            name='target_mode',
            field=models.IntegerField(default=0),
        ),
    ]

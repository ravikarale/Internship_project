# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-11 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpcm',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='addpcm',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]

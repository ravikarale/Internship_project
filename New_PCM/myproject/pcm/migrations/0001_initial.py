# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-15 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pcm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.IntegerField()),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('emailId', models.EmailField(max_length=254)),
                ('xth', models.FloatField()),
                ('xiith', models.FloatField()),
                ('graduation', models.FloatField()),
                ('cgpa', models.FloatField()),
                ('status', models.CharField(default='unplace', max_length=20)),
            ],
        ),
    ]

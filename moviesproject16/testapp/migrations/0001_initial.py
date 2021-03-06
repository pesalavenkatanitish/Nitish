# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-12-23 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.CharField(max_length=30)),
                ('MovieName', models.CharField(max_length=30)),
                ('Hero', models.CharField(max_length=30)),
                ('Heroine', models.CharField(max_length=30)),
                ('Rating', models.IntegerField()),
            ],
        ),
    ]

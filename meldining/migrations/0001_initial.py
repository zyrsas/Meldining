# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-16 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('file', models.FileField(upload_to='', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='CuisineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('file', models.FileField(upload_to='', verbose_name='Image')),
                ('description', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('tel', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160527_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('bigpicture', models.CharField(max_length=200)),
                ('smpicture', models.CharField(max_length=200)),
                ('showpictures', models.CharField(max_length=200)),
                ('small_desc', models.TextField(max_length=1000)),
                ('main_desc', models.TextField(max_length=20000)),
                ('feature_desc', models.TextField(max_length=20000)),
                ('type_tags', models.CharField(max_length=200)),
                ('IOS_link', models.CharField(max_length=100)),
                ('ANDROID_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Games',
        ),
    ]
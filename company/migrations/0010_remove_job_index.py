# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_job_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='index',
        ),
    ]

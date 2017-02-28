# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 05:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20160528_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='picture',
            new_name='smpicture',
        ),
        migrations.AddField(
            model_name='new',
            name='bigpicture',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 28, 5, 33, 7, 736202, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
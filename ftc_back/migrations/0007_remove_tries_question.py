# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftc_back', '0006_auto_20160919_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tries',
            name='Question',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

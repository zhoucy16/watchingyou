# Generated by Django 2.1 on 2018-09-14 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0013_alert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='camera',
        ),
    ]
# Generated by Django 2.1 on 2018-09-13 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0004_auto_20180912_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

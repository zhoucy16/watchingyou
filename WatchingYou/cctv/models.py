# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    isSuperUser = models.BooleanField(default=False)

    password_en = models.BooleanField(default=False)

    encrypt_items = ['password']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        for attr in self.encrypt_items:
            if not getattr(self, '%s_en' % attr):
                self.__setattr__(attr, make_password(getattr(self, attr)))
                self.__setattr__('%s_en' % attr, True)
        super(User, self).save(*args, **kwargs)

    def is_password_right(self, password):
        return check_password(password, self.password)

class Camera(models.Model):
    camera_id = models.CharField(max_length=200, unique=True)
    camera_info = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.camera_id

class Image(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')
    camera = models.ForeignKey(Camera, to_field='camera_id', on_delete=models.CASCADE, default=0)
    detection_type = models.CharField(max_length=20, default='None')

    def __str__(self):
        return str(self.add_time)

    def was_load_recently(self):
        return self.add_time > timezone.now() - datetime.timedelta(seconds=2)

class Alert(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    camera = models.ForeignKey(Camera, to_field='camera_id', on_delete=models.CASCADE, default=0)
    message = models.TextField()

    def __str__(self):
        return str(self.add_time) + ' ' + str(self.message)

@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    instance.img.delete(False)



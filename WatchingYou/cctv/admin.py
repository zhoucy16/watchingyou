# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Image, Camera, Alert

admin.site.register(User)
admin.site.register(Image)
admin.site.register(Camera)
admin.site.register(Alert)

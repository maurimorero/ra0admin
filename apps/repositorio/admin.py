# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import EstadoPublicacion,Publicacion,Revision

# Register your models here.

admin.site.register(EstadoPublicacion)
admin.site.register(Publicacion)
admin.site.register(Revision)

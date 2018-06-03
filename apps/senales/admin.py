# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Senal,TipoConexion,Conexion, Bornera

admin.site.register(Senal)
admin.site.register(TipoConexion)
admin.site.register(Conexion)
admin.site.register(Bornera)

admin.autodiscover()

# Register your models here.

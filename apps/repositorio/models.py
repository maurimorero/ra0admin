# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..usuarios.models import Profile

# Create your models here.

class EstadoPublicacion(models.Model):
	nombre = models.CharField(max_length=400)
	descripcion = models.TextField(blank=True, null=True,default=None)

	def __str__(self):
		return (self.nombre)

class Publicacion(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    codificacion = models.CharField(max_length=400,null=True, default=None, blank=True)
    nombreDoc = models.CharField(max_length=400,  unique=True)
    formato = models.CharField(max_length=400)
    fechaActualizacion = models.DateTimeField(auto_now_add=True)
    ubicacion = models.CharField(max_length=400)
    estado = models.ForeignKey(EstadoPublicacion, default=None)

    def __str__(self):
		return (self.nombreDoc)

class Revision(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    orden = models.IntegerField()
    comentarios = models.TextField(blank=True, null=True, default=None)
    publicacion = models.ForeignKey(Publicacion)
    usuario = models.ForeignKey(Profile)
    completada = models.BooleanField(default=False, blank=True)

    def __str__(self):
		return (str(self.fecha)+' - '+str(self.publicacion.nombreDoc))
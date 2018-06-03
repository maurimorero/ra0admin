# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Chasis(models.Model):
	name = models.CharField(max_length=400, unique=True)
	description = models.TextField(blank=True, null=True,default=None)

	def __str__(self):
		return (self.name)

class TipoConexion(models.Model):
	name = models.CharField(max_length=400)
	description = models.TextField(blank=True, null=True,default=None)

	def __str__(self):
		return (self.name)

class Senal (models.Model):
	codigo = models.CharField(max_length=400)
	nombre  = models.CharField(max_length=400)
	tipoSenal = models.CharField(max_length=400)
	rango = models.CharField(max_length=400)
	comentarios = models.TextField(blank=True, null=True,default=None)

	def __str__(self):
		return (self.codigo)

class Bornera(models.Model):
	name = models.CharField(max_length=400, unique=True)
	description = models.TextField(blank=True, null=True,default=None)

	def __str__(self):
		return (self.name)


class Conexion(models.Model):
	bornera = models.ForeignKey(Bornera)
	chasis = models.ForeignKey(Chasis,default=None)
	conector = models.CharField(max_length=400,default=None)
	pin = models.CharField(max_length=400)
	orden = models.IntegerField()
	descripcion = models.TextField(blank=True, null=True,default=None)
	tipoConexion = models.ForeignKey(TipoConexion)
	senal = models.ForeignKey(Senal)

	def __str__(self):
		return (str(self.bornera) +" - "+str(self.pin))
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_auto_20170418_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoPublicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
                ('descripcion', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('codificacion', models.CharField(max_length=400)),
                ('nombreDoc', models.CharField(max_length=400)),
                ('formato', models.CharField(max_length=400)),
                ('fechaActualizacion', models.DateTimeField(auto_now_add=True)),
                ('ubicacion', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('orden', models.IntegerField()),
                ('comentarios', models.TextField(blank=True, default=None, null=True)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repositorio.Publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Profile')),
            ],
        ),
    ]

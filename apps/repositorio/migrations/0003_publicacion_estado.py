# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0002_revision_completada'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='estado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='repositorio.EstadoPublicacion'),
        ),
    ]
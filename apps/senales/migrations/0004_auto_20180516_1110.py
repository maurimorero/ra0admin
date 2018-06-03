# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('senales', '0003_auto_20170515_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chasis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='conexion',
            name='conector',
            field=models.CharField(default=None, max_length=400),
        ),
        migrations.AddField(
            model_name='conexion',
            name='chasis',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='senales.Chasis'),
        ),
    ]
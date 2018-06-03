# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from forms import SenalForm, BorneraForm, ConexionForm, ChasisForm
from models import Senal, Conexion, Bornera, Chasis
from django.contrib import messages

# Create your views here.

def Nueva(request):
    if request.method == 'POST':
        senalform = SenalForm(request.POST)

        if senalform.is_valid():
            senal=senalform.save()
            messages.success(request, 'Senal creada exitosamente!')
            return redirect('senales_home')
    else:
        senalform = SenalForm()
    return render(request, 'nuevasenal.html', {
        'senalform': senalform,
    })

def NuevaBornera(request):
    if request.method == 'POST':
        borneraForm = BorneraForm(request.POST)

        if borneraForm.is_valid():
            bornera=borneraForm.save()
            messages.success(request, 'Bornera creada exitosamente!')
            return redirect('senales_home')
    else:
        borneraForm = BorneraForm()
    return render(request, 'nuevabornera.html', {
        'borneraForm': borneraForm,
    })

def ActualizaSenal(request,id):
    if request.method == 'POST':
        instance = get_object_or_404(Senal, id=id)
        senalform = SenalForm(request.POST, instance=instance)
        if senalform.is_valid():
            senal=senalform.save()
            messages.success(request, 'Senal actualizada exitosamente!')
            return redirect('senales_home')
    else:
        senal= Senal.objects.get(id=id)
        senalform = SenalForm(instance=senal)
        conexiones = Conexion.objects.filter(senal=senal)
    return render(request, 'actualizasenal.html', {
        'senalform': senalform,
        'conexiones':conexiones,
        'senal':senal,
    })

def EliminaConexion(request,ids,idc):
    conexion = Conexion.objects.get(id=idc)
    conexion.delete()
    return ActualizaSenal(request, ids)

def NuevaConexion(request, id):
    if request.method == 'POST':
        conexionForm = ConexionForm(request.POST)

        if conexionForm.is_valid():
            conexion=conexionForm.save(commit=False)
            senal=Senal.objects.get(id=id)
            conexion.senal=senal
            conexion.save()
            messages.success(request, 'Conexion creada exitosamente!')
            return redirect('senales:actualizasenal', id=senal.id)
    else:
        conexionForm = ConexionForm()
    return render(request, 'nuevaconexion.html', {
        'conexionForm': conexionForm,
    })

def ConexionesBornera(request,id):
    bornera = Bornera.objects.get(id=id)
    conexiones= Conexion.objects.filter(bornera=bornera)
    return render(request, 'conexionesbornera.html', {'bornera':bornera,
                                                    'conexiones':conexiones})


def NuevoChasis(request):
    if request.method == 'POST':
        chasisForm = ChasisForm(request.POST)

        if chasisForm.is_valid():
            chasis=chasisForm.save()
            messages.success(request, 'Chasis creada exitosamente!')
            return redirect('senales_home')
    else:
        chasisForm = ChasisForm()
    return render(request, 'nuevochasis.html', {
        'chasisForm': chasisForm,
    })
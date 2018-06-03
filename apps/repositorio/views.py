# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from forms import PublicacionForm, RevisionForm, RevisarForm
from django.contrib import messages
from models import Publicacion, EstadoPublicacion, Revision
import datetime
from ..usuarios.models import Profile


def Nuevo(request):
    if request.method == 'POST':
        publicacionForm = PublicacionForm(request.POST)

        if publicacionForm.is_valid():
            estados= EstadoPublicacion.objects.filter(nombre__iexact="Elaborado")
            estado = estados[0]
            publicacion=publicacionForm.save(commit=False)
            publicacion.estado=estado
            publicacion.save()
            messages.success(request, 'Publicacion creada exitosamente!')
            return redirect('repositorio_home')
    else:
        publicacionForm = PublicacionForm()
    return render(request, 'nuevapublicacion.html', {
        'publicacionForm': publicacionForm,
    })

def ActualizaPublicacion(request,id):
    if request.method == 'POST':
        instance = get_object_or_404(Publicacion, id=id)
        publicacionForm = PublicacionForm(request.POST, instance=instance)
        if publicacionForm.is_valid():
            publicacion=publicacionForm.save()
            messages.success(request, 'Publicacion actualizada exitosamente!')
            return redirect('repositorio_home')
    else:
        publicacion= Publicacion.objects.get(id=id)
        publicacionForm = PublicacionForm(instance=publicacion)
        revisiones = Revision.objects.filter(publicacion=publicacion)
        estado=0
        if(publicacion.estado.nombre == 'Elaborado'):
            estado = 1
        if (publicacion.estado.nombre == 'En revisión'):
            estado = 2
        if (publicacion.estado.nombre == 'En codificación'):
            estado = 3
        if (publicacion.estado.nombre == 'Aprobado'):
            estado = 4
    return render(request, 'actualizapublicacion.html', {
        'publicacionForm': publicacionForm,
        'revisiones':revisiones,
        'publicacion':publicacion,
        'estado':estado,
    })

def EliminaRevision(request,idp,idr):
    revision = Revision.objects.get(id=idr)
    revision.delete()
    return ActualizaPublicacion(request, idp)


def NuevaRevision(request, idp):
    if request.method == 'POST':
        revisionForm = RevisionForm(request.POST)

        if revisionForm.is_valid():
            publicacion= Publicacion.objects.get(id=idp)
            revision=revisionForm.save(commit=False)
            revision.publicacion=publicacion
            revision.save()
            messages.success(request, 'Revisión creada exitosamente!')
            return redirect('repositorio:actualizapublicacion', id=idp)
    else:
        revisionForm = RevisionForm()
    return render(request, 'nuevarevision.html', {
        'revisionForm': revisionForm,
    })

def FinalizarElaboracion(request,idp):
    publicacion = Publicacion.objects.get(id=idp)
    revisiones = Revision.objects.filter(publicacion=publicacion)
    if(len(revisiones)<1):
        messages.error(request, 'La publicación debe tener, al menos, una revisión')
        return ActualizaPublicacion(request, idp)
    estado= EstadoPublicacion.objects.filter(nombre__iexact='En revisión')
    publicacion.estado=estado[0]
    publicacion.save()
    return ActualizaPublicacion(request, idp)

def Revisar(request,idp):
    if request.method == 'POST':
        publicacion = Publicacion.objects.get(id=idp)
        revisiones = Revision.objects.filter(publicacion=publicacion, completada=False)
        perfil = Profile.objects.filter(user=request.user)
        cuenta=0
        for rev in revisiones:
            cuenta=cuenta+1
            if rev.usuario.user == perfil[0].user :
                instance=rev
        revisionForm = RevisarForm(request.POST, instance=instance)
        if revisionForm.is_valid():
            revision=revisionForm.save(commit=False)
            revision.completada=True
            revision.fecha=  datetime.datetime.now()
            revision.save()
            if cuenta==1:
                estado = EstadoPublicacion.objects.filter(nombre__iexact='En codificación')
                publicacion.estado = estado[0]
                publicacion.save()
            messages.success(request, 'Revisión actualizada exitosamente!')
            return redirect('repositorio:actualizapublicacion', id=idp)
    else:
        publicacion= Publicacion.objects.get(id=idp)
        revisiones= Revision.objects.filter(publicacion=publicacion, completada=False)
        perfil= Profile.objects.filter(user=request.user)
        print "Usuario="+perfil[0].user.username
        print "Usuario="+request.user.username
        bandera=0
        for rev in revisiones:
            if rev.usuario.user == perfil[0].user :
                revision=rev
                bandera=1
        if bandera==0:
            messages.error(request, 'No existen revisiones pendientes para su usuario!')
            return redirect('repositorio:actualizapublicacion', id=idp)

        revisionForm = RevisarForm(instance=revision)

    return render(request, 'revisar.html', {
        'revisionForm': revisionForm,
        'revision':revision,
        'publicacion':publicacion,
    })

def Aprobar(request, idp):
    publicacion = Publicacion.objects.get(id=idp)
    estado = EstadoPublicacion.objects.filter(nombre__iexact='Aprobado')
    publicacion.estado = estado[0]
    publicacion.save()
    return redirect('repositorio:actualizapublicacion', id=idp)
# -*- coding: utf-8 -*-
from django import forms
from models import Revision,EstadoPublicacion, Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [
            'nombreDoc',
            'formato',
            'ubicacion',
            'codificacion',
        ]
        labels = {
            'nombreDoc': 'Nombre del documento',
            'formato':'Formato',
            'ubicacion': 'Ubicacion',
            'codificacion':'Codificacion',
        }

class RevisionForm(forms.ModelForm):
    class Meta:
        model = Revision
        fields = [
            'orden',
            'usuario',
        ]
        labels = {
            'orden': 'Orden',
            'usuario':'Revisor',
        }

class RevisarForm(forms.ModelForm):
    class Meta:
        model = Revision
        fields = [
            'comentarios'
        ]
        labels = {
            'comentarios': 'Comentarios',
        }
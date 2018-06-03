from django import forms
from models import Senal, TipoConexion,Conexion, Bornera, Chasis

class SenalForm(forms.ModelForm):
    class Meta:
        model = Senal
        fields = [
            'codigo',
            'nombre',
            'tipoSenal',
            'rango',
            'comentarios',
        ]
        labels = {
            'codigo': 'Codigo',
            'nombre':'Nombre',
            'tipoSenal': 'Tipo de senal',
            'rango':'Rango',
            'comentarios':'Comentarios',
        }

class BorneraForm(forms.ModelForm):
    class Meta:
        model = Bornera
        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': 'Nombre',
            'description':'Descripcion',
        }

class ConexionForm(forms.ModelForm):
    class Meta:
        model = Conexion
        fields = [
            'chasis',
            'bornera',
            'conector',
            'pin',
            'orden',
            'descripcion',
            'tipoConexion',
        ]
        labels = {
            'chasis': 'Chasis',
            'bornera':'Bornera',
            'conector':'Conector',
            'pin':'Pin',
            'orden':'Orden',
            'descripcion':'Descripcion',
            'tipoConexion':'Tipo de Conexion',
        }

class ChasisForm(forms.ModelForm):
    class Meta:
        model = Chasis
        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': 'Nombre',
            'description':'Descripcion',
        }
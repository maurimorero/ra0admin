from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from models import Profile

class RegistroForm (UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
        ]
        labels = {
            'username':'Nombre de usuario',
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
        ]
        labels = {
            'username': 'Nombre de usuario',
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('organizacion',
                  'nombre',
                  'email',
                  'puesto',
                  'provincia',
                  'localidad',
                  'direccion',
                  'telefono',
                  )
        labels = {
            'organizacion': 'Organizacion',
            'nombre':'Nombre completo',
            'email':'E-mail',
            'puesto':'Puesto',
            'provincia':'Provincia',
            'localidad':'Localidad',
            'direccion':'Direccion',
            'telefono':'Telefono',
        }
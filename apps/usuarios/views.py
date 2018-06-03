from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from forms import RegistroForm,ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
from django.contrib import messages
from ..senales.models import Senal, Bornera
from ..repositorio.models import Publicacion


#class RegistroUsuario(CreateView):
#    model= User
#    template_name= "usuarios/registrar.html"
#    form_class = RegistroForm
#    second_form_class= ProfileForm
#    success_url = reverse_lazy('usuarios:usuarios_home')

def RegistroUsuario(request):
    if request.method == 'POST':
        user_form = RegistroForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            usuario=user_form.save()
            profile_form = ProfileForm(request.POST, instance=usuario.profile)
            profile_form.save()
            messages.success(request, 'Usuario creado exitosamente!')
            return redirect('usuarios:usuarios_home')
    else:
        user_form = RegistroForm()
        profile_form = ProfileForm()
    return render(request, 'usuarios/registrar.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def UserHome(request):
    if request.method == 'POST':
        if (request.POST.get("tipobusqueda", "") == '1'):
            return BusquedaBornera(request=request)
        if (request.POST.get("tipobusqueda", "") == '2'):
            return BusquedaSenal(request=request)
        #print (request.POST.get("campobusqueda", ""))
        senales = Senal.objects.all()
        return render(request, 'home.html', {'senales': senales})

    senales = Senal.objects.all().order_by('nombre')
    publicaciones = Publicacion.objects.all().order_by('nombreDoc')
    return render(request,'home.html',{'senales':senales,'publicaciones':publicaciones})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('usuarios:usuarios_home')
        #else:
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'usuarios/actualizar.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def BusquedaSenal(request):
    print (request.POST.get("campobusqueda", ""))
    senales = Senal.objects.filter(nombre__iexact=request.POST.get("campobusqueda", ""))
    senales1 = Senal.objects.filter(codigo__iexact=request.POST.get("campobusqueda", ""))
    return render(request, 'busquedasenal.html', {'senales':senales,
                                                  'senales1':senales1})

def BusquedaBornera(request):
    print (request.POST.get("campobusqueda", ""))
    borneras = Bornera.objects.filter(name__iexact=request.POST.get("campobusqueda", ""))
    return render(request, 'busquedabornera.html', {'borneras':borneras})

def HomeSenales(request):
    if request.method == 'POST':
        if (request.POST.get("tipobusqueda", "") == '1'):
            return BusquedaBornera(request=request)
        if (request.POST.get("tipobusqueda", "") == '2'):
            return BusquedaSenal(request=request)
        #print (request.POST.get("campobusqueda", ""))
        senales = Senal.objects.all()
        return render(request, 'homesenales.html', {'senales': senales})

    senales = Senal.objects.all().order_by('nombre')
    publicaciones = Publicacion.objects.all().order_by('nombreDoc')
    return render(request,'homesenales.html',{'senales':senales,'publicaciones':publicaciones})

def HomeRepositorio(request):
    if request.method == 'POST':
        if (request.POST.get("tipobusqueda", "") == '1'):
            return BusquedaBornera(request=request)
        if (request.POST.get("tipobusqueda", "") == '2'):
            return BusquedaSenal(request=request)
        #print (request.POST.get("campobusqueda", ""))
        senales = Senal.objects.all()
        return render(request, 'homerepositorio.html', {'senales': senales})

    senales = Senal.objects.all().order_by('nombre')
    publicaciones = Publicacion.objects.all().order_by('nombreDoc')
    return render(request,'homerepositorio.html',{'senales':senales,'publicaciones':publicaciones})
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from views import Nuevo, ActualizaPublicacion, EliminaRevision, NuevaRevision, FinalizarElaboracion, Revisar, Aprobar

urlpatterns = [
    url(r'^nuevo/', login_required(Nuevo), name="nuevo"),
    url(r'^actualizapublicacion/(?P<id>\d+)/$', login_required(ActualizaPublicacion), name='actualizapublicacion'),
    url(r'^eliminarevision/(?P<idp>\d+)/(?P<idr>\d+)/$', login_required(EliminaRevision), name='eliminarevision'),
    url(r'^nuevarevision/(?P<idp>\d+)/$', login_required(NuevaRevision), name='nuevarevision'),
    url(r'^finalizarelaboracion/(?P<idp>\d+)/$', login_required(FinalizarElaboracion), name='finalizarelaboracion'),
    url(r'^revisar/(?P<idp>\d+)/$', login_required(Revisar), name='revisar'),
    url(r'^aprobar/(?P<idp>\d+)/$', login_required(Aprobar), name='aprobar'),
]

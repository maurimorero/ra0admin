from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from views import Nueva, NuevaBornera, ActualizaSenal, EliminaConexion, NuevaConexion, ConexionesBornera, NuevoChasis

urlpatterns = [
    url(r'^nueva/', login_required(Nueva), name="nueva"),
    url(r'^nuevabornera/', login_required(NuevaBornera), name="nuevabornera"),
    url(r'^nuevochasis/', login_required(NuevoChasis), name="nuevochasis"),
    url(r'^actualizasenal/(?P<id>\d+)/$', login_required(ActualizaSenal), name='actualizasenal'),
    url(r'^eliminaconexion/(?P<ids>\d+)/(?P<idc>\d+)/$', login_required(EliminaConexion), name='eliminaconexion'),
    url(r'^nuevaconexion/(?P<id>\d+)/$', login_required(NuevaConexion), name="nuevaconexion"),
    url(r'^conexionesbornera/(?P<id>\d+)/$', login_required(ConexionesBornera), name="conexionesbornera"),
]

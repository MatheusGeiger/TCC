from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views
import app.views

urlpatterns = [
    url(r'^$', app.views.lista_viagem, name='lista_viagem'),
    url(r'^viagem/(?P<id_viagem>[A-Za-z0-9-\/]+)/$', app.views.viagem, name='viagem'),
    url(r'^viagem/add_viagem/$', app.views.add_viagem, name='add_viagem'),
    url(r'^viagem/iniciar_viagem/(?P<id_viagem>[A-Za-z0-9-\/]+)/(?P<latitude>[.A-Za-z0-9-\/]+)/(?P<longitude>[.A-Za-z0-9-\/]+)/$', app.views.iniciar_viagem, name='iniciar_viagem'),
    url(r'^viagem/finalizar_viagem/(?P<id_viagem>[A-Za-z0-9-\/]+)/(?P<latitude>[.A-Za-z0-9-\/]+)/(?P<longitude>[.A-Za-z0-9-\/]+)/$', app.views.finalizar_viagem, name='finalizar_viagem'),
    url(r'^viagem/cancelar_viagem/(?P<id_viagem>[A-Za-z0-9-\/]+)/$', app.views.cancelar_viagem, name='cancelar_viagem'),
    url(r'^lista_viagem/$', app.views.lista_viagem, name='lista_viagem'),
    # url(r'^ocorrencia/$', app.views.ocorrencia, name='ocorrencia'),
    url(r'^lista_motorista/$', app.views.lista_motorista, name='lista_motorista'),
    url(r'^motorista/add_motorista/$', app.views.add_motorista, name='add_motorista'),
    url(r'^lista_veiculo/$', app.views.lista_veiculo, name='lista_veiculo'),
    url(r'^veiculo/add_veiculo/$', app.views.add_veiculo, name='add_veiculo'),
    url(r'^lista_ocorrencia/$', app.views.lista_ocorrencia, name='lista_ocorrencia'),
    url(r'^insere_ocorrencia/(?P<id_viagem>[.A-Za-z0-9-\/]+)/(?P<latitude>[.A-Za-z0-9-\/]+)/(?P<longitude>[.A-Za-z0-9-\/]+)/$', app.views.insere_ocorrencia, name='insere_ocorrencia'),
    url(r'^insere_coordenada/veiculo/(?P<latitude>[.A-Za-z0-9-\/]+)/(?P<longitude>[.A-Za-z0-9-\/]+)/(?P<status_porta>[.A-Za-z0-9-\/]+)/$', app.views.insere_coordenada, name='insere_coordenada'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]

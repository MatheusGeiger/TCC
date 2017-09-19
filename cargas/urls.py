from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views
import app.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^viagem/$', app.views.viagem, name='viagem'),
    url(r'^ocorrencia/$', app.views.ocorrencia, name='ocorrencia'),
    url(r'^db', app.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]

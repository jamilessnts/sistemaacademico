from django.conf.urls import url, include #permite incluir urls
from django.contrib import admin
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('sistemaacademico.urls')),


]


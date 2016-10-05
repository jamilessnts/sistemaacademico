from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index), # o name=index nao é obrigatório mas é bastante útil
]
from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^error/$', views.errorlogin, name='error_login'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^professor/inicial$', views.inicialprofessor, name='inicialp'),
    url(r'^aluno/inicial$', views.inicialaluno),
    url(r'^aluno/inicial/notas$', views.notaAlunoLogago, name='aluno_nota'),
    url(r'^aluno/inicial/historico$', views.historicoAlunoLogado, name='aluno_historico'),
    url(r'^professor/inicial/grafico$', views.graficoteste, name='grafico'),
    url(r'^professor/inicial/notas$', views.NotaTodosAlunos.as_view()),
    url(r'^professor/inicial/pdf$', views.export_csv),



]
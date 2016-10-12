from django.conf.urls import include, url
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^professor/$', views.professor, name='professor'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^professor/inicial$', views.inicialprofessor),
    url(r'^aluno/$', views.aluno),
    url(r'^aluno/inicial$', views.inicialaluno),
    url(r'^professor/inicial/notas$', views.NotaTodosAlunos.as_view()),

    #url(r'^login/$', views.LoginView.as_view, name='login'),  # alterar para view de login
    #url(r'^logout/$', views.LogoutView.as_view, name='logout'),  # alterar para view de login

]
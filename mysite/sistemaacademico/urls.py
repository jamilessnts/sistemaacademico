from django.conf.urls import include, url
from . import views


urlpatterns = [
    #url para página incial
    url(r'^$', views.index, name='index'), # o name=index nao é obrigatório mas é bastante útil

    # urls para página dos professores
    url(r'^professor/$', views.professor, name='professor'), # essa variavel nome permite que possamos usa-la no template de 'forma
    #mais dinamica. se no futuro o url mudar, so preciso mudar aqui, e todos os lugares que usa essa url irá ser atualizada

    # #urls para página dos alunos
    url(r'^aluno/$', views.aluno, name='aluno'),

]
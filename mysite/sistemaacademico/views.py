from django.http import HttpResponse #no futuro nao iremos precisar desse import pq estou usando render
from django.shortcuts import render
from django.http import Http404 #mostrar erros


#no arquivo Html quando for colocar codigo python é feito com {% ....%}
# se for variaveis eu utilizo {{nome da variavel}}

from .models import Curso
#
#Dica para verificar o que tem nas tabelas pelo queryShell
# python manage.py shell -> from sistemaacademico.models import 'nomedaTabela'
#select * = Curso.objects.all()


# home page
def index(request):
    return render(request, 'sistemaacademico/site_homepage.html')

# pagina do professor

def professor(request):
    cursos = Curso.objects.all()
    context = {'cursos':cursos} # fazer um dicionario para simplificar o codigo
    return render(request, 'sistemaacademico/aluno_pagina_inicial.html', context)


def aluno(request):
    cursos = Curso.objects.all()
    return render(request, 'sistemaacademico/curso_list.html', {'cursos':cursos})

# fazer um for no arquivo hmtl
# e mostrar o detalhe de cada estudante por exemplo - mostra os estudantes e fica em formato de link
#e ao clicar em cada estudante é possivel ver detalhes sobre ele

#{% if all_albuns %}
#     <ul>
#        {% for album in all_albums %}
#           <li><a> href="/music/{{album_id}}/">{{album.album_title}}</a></li>
#      </ul>
#       {% endfor %}
#
#

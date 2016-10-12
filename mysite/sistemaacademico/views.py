from .models import Avaliacoes, Disciplina, Curso, Turma
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate
from django.shortcuts import render


from django.views import generic

# home page
def index(request):
    return render(request, 'sistemaacademico/site_homepage.html')


# pagina inicial de login do professor
def professor(request):
    return render(request, 'sistemaacademico/professor_login.html')


# pagina inicial do professor
def inicialprofessor(request):
    return render(request, 'sistemaacademico/professor_inicial.html')


# pagina login do aluno
def aluno(request):
    return render(request, 'sistemaacademico/aluno_login.html')

def sobre(request):
    return render(request, 'sistemaacademico/sobre.html')


# pagina inicial do aluno
def inicialaluno(request):
    cursos = Curso.objects.all()
    context = {'notas':Avaliacoes}
    return render(request, 'sistemaacademico/aluno_inicial.html', context)

def get_user(request):
    current_user = request.get.user
    return current_user


class NotaTodosAlunos(generic.ListView):
    template_name = 'sistemaacademico/notas_todos_alunos.html'
    context_object_name = 'lista_notas'

    def get_queryset(self):
        return Avaliacoes.objects.all()


























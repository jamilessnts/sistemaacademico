from .models import Avaliacoes, Disciplina, Curso, Turma
from django.http import *
from django.shortcuts import render_to_response, render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User


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

def errorlogin(request):
    return render(request, 'sistemaacademico/error.html')

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


def login_user(request):

    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.groups.filter(name='professor'):
                    return HttpResponseRedirect('/professor/inicial')
                else:
                    return HttpResponseRedirect('/aluno/inicial')
    return render(request, 'sistemaacademico/login.html')


def logout_view(request):
    logout(request)
    return render (request, 'sistemaacademico/site_homepage.html')






















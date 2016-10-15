from .models import Avaliacoes, Disciplina, Curso, Turma, Historico
from django.http import *
from django.shortcuts import render_to_response, render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic
from django.db.models import Sum
from django.shortcuts import render
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse




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


class NotaTodosAlunos(generic.ListView):
    template_name = 'sistemaacademico/notas_todos_alunos.html'
    context_object_name = 'lista_notas'

    def get_queryset(self):
        return Avaliacoes.objects.all()


# Funções para Login e logout
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
                elif user.is_superuser:
                    return HttpResponseRedirect('/admin')
                else:
                    return HttpResponseRedirect('/aluno/inicial')
    return render(request, 'sistemaacademico/login.html')


def logout_view(request):
    logout(request)
    return render (request, 'sistemaacademico/site_homepage.html')


def notaAlunoLogago(request):
    current_user = request.user
    lista_nota = Avaliacoes.objects.filter(aluno=request.user)
    context = {'lista_nota':lista_nota}
    return render(request, 'sistemaacademico/nota_aluno_logado.html', context)


def graficoteste(request):
    total_n1 = Avaliacoes.objects.all().aggregate(Sum('nota1'))
    total_n2 = Avaliacoes.objects.all().aggregate(Sum('nota2'))
    context = {'total_n1': total_n1}
    total_n3 = Avaliacoes.objects.all().aggregate(Sum('nota3'))
    return render(request, 'sistemaacademico/grafico.html', {'total_n1': total_n1, 'total_n2': total_n2, 'total_n3': total_n3})

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=notadosalunos.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Aluno"),
        smart_str(u"Disciplina"),
        smart_str(u"Nota1"),
        smart_str(u"Nota2"),
        smart_str(u"Nota3"),
    ])
    queryset = Avaliacoes.objects.all()

    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.aluno),
            smart_str(obj.disciplina),
            smart_str(obj.nota1),
            smart_str(obj.nota2),
            smart_str(obj.nota3),
        ])
    return response
export_csv.short_description = u"Export CSV"


def historicoAlunoLogado(request):
    current_user = request.user
    lista_nota = Historico.objects.filter(aluno=request.user)
    context = {'lista_nota':lista_nota}
    return render(request, 'sistemaacademico/historico_aluno.html', context)


















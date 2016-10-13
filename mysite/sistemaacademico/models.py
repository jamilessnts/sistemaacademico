from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
import json


# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    curso = models.ForeignKey('Curso')

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    disciplina = models.ForeignKey('Disciplina')
    professor = models.ForeignKey('auth.User', limit_choices_to={'groups':'1'})

    def __str__(self):
        return self.nome

class Avaliacoes(models.Model):
    aluno = models.ForeignKey('auth.User', limit_choices_to={'groups':2})
    disciplina = models.ForeignKey('Disciplina')
    #professor = models.ForeignKey('auth.User', limit_choices_to={'groups':1}) # para retornar o professor que lancou a nota
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        permissions = (
            ('readonly', 'Can Read only Avaliacoes'),
        )


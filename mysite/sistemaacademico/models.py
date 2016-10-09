from django.db import models
from django.utils import timezone

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey('Curso')

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    disciplina = models.ForeignKey('Disciplina')
    professor = models.ForeignKey('auth.User')

    def __str__(self):
        return self.nome

class Avaliacoes(models.Model):
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2)
    disciplina = models.ForeignKey('Disciplina')
    aluno = models.ForeignKey('auth.User')


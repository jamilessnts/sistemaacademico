from django.contrib import admin
from .models import Curso, Disciplina, Turma, Avaliacoes

# Register your models here.

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Avaliacoes)



from django.contrib import admin
from .models import Curso, Disciplina, Turma, Avaliacoes, Historico

# Register your models here.

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'professor')
    search_fields = ('nome', 'disciplina')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso')


class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina','nota1', 'nota2', 'nota3' )
    list_filter = ('aluno', 'disciplina')

class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina','media')
    list_filter = ('aluno', 'disciplina')

admin.site.register(Curso)
admin.site.register(Historico, HistoricoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Avaliacoes, NotaAdmin)






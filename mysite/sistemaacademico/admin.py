from django.contrib import admin
from .models import Curso, Disciplina, Turma, Avaliacoes

# Register your models here.

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'professor')
    search_fields = ('nome', 'disciplina')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso')


class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina','nota1', 'nota2', 'nota3' )
    list_filter = ('aluno', 'disciplina')
    actions = ['accept', 'reject', 'peding']


class ReadonlyNotasAdmin(NotaAdmin):
    def __init__(self, model, admin_site):
        super(ReadonlyNotasAdmin, self).__init__(model, admin_site)
        self.model = model

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('avaliacao.readonly') and not request.user.is_superuser:
            return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.has_perm('avaliacao.readonly') and not request.user.is_superuser:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.has_perm('avaliacao.readonly') and not request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = ()
            return True
        elif request.user.has_perm('avaliacao.readonly'):
            self.readonly_fields = [field.name for field in filter (lambda f: not f.auto_created, self.model._meta.fields)]
            return  True
        else:
            return False


    def get_actions(self, request):
        actions = super(ReadonlyNotasAdmin, self).get_actions(request)
        if request.user.has_perm('avaliacao.readonly') and not request.user.is_superuser:
            if 'delete_selected' in actions:
                del actions ['delete_selected']
                del actions ['accept']
                del actions['reject']
                del actions['pending']
            return actions
        else:
            return actions


admin.site.register(Curso)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Avaliacoes, ReadonlyNotasAdmin)






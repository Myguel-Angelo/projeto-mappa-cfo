from django.contrib import admin
from anotacao.models import TurmaCadetes, UserMilitar, Anotacao, ArquivoExportado

@admin.register(TurmaCadetes)
class TurmaCadetesAdmin(admin.ModelAdmin):
    list_display = ('turma',)
    
@admin.register(UserMilitar)
class UserMilitarAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'turma', 'numerica')

@admin.register(Anotacao)
class AnotacaoAdmin(admin.ModelAdmin):
    list_display = ('criado_por', 'cadete_anotado', 'tipo_anotacao', 'status', 'criada_em', 'despacho')

@admin.register(ArquivoExportado)
class ArquivoExportadoAdmin(admin.ModelAdmin):
    list_display = ('nome_arquivo',)
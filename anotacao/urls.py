from django.urls import path
from anotacao import views
from django.conf import settings
from django.conf.urls.static import static
# URLS centaris do app

urlpatterns = [
    path('login/', views.login_view, name='login'), # Rota de login
    path('logout/', views.logout_view, name='logout'), # Rota de logout
    path('', views.home_view, name='home'), # Rota da home inicial
    path('alterar-senha/', views.alterar_senha_view, name='alterar_senha'), # Rota para alterar senha
    path('anotacoes/', views.cadete_anotacoes_view, name='cadete_anotacoes'), # Rota das anotações pessoais dos cadetes
    path('cadetes/', views.lista_cadetes_view, name='lista_cadetes'), # Rota da relação de cadetes para anotar
    path('criar-anotacao_ajax/', views.criar_anotacao_ajax_view, name='criar_anotacao_ajax'), # Rota para criação de anotações
    path('comandante-anotacoes/', views.comandante_anotacoes_view, name='comandante_anotacoes'),  # Rota para o oficial comandante
    path('comandante-anotacoes/despachar_ajax/<int:anotacao_id>/', views.despachar_anotacao_ajax_view, name='despachar_anotacao_ajax'),  # Rota para despachar anotações
    path('comandante-anotacoes/anotacoes/excluir/<int:anotacao_id>/', views.excluir_anotacao_view, name='excluir_anotacao'),
    path('anotacoes-despachadas', views.anotacoes_despachadas_view, name='anotacoes_despachadas'),  # Rota para despachar anotações
    path('historico_exportacoes/', views.historico_exportacoes_view, name='historico_exportacoes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),        # <- página inicial = login
    path('home/', views.home, name='home'),           # <- home vai pra /home
    path('escadas/', views.lista_escadas, name='lista_escadas'),
    path('escadas/criar/', views.criar_escada, name='criar_escada'),
    path('escadas/<int:id>/', views.detalhe_escada, name='detalhe_escada'),
    path('escadas/<int:id>/status/', views.atualizar_status, name='atualizar_status'),
    path('status/', views.status_escadas, name='status_escadas'),
    path('escadas/<int:id>/concluir/', views.concluir_escada, name='concluir_escada'),
    path('api/escadas/', views.api_lista_escadas, name='api_lista_escadas'),
    path('escadas/<int:id>/deletar/', views.deletar_escada, name='deletar_escada'),
    path('logout/', views.logout_view, name='logout'),
]
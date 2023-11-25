from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('deletar/<int:id>/', views.deletar_livro, name='deletar_livro'),
]
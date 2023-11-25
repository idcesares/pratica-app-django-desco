from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})


def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/adicionar_livro.html', {'form': form})


def editar_livro(request, id):
    livro = Livro.objects.get(pk=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/editar_livro.html', {'form': form, 'livro': livro})


def deletar_livro(request, id):
    Livro.objects.get(pk=id).delete()
    return redirect('listar_livros')
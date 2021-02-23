from django.shortcuts import render, redirect
from .models import Categoria
from .form_categoria import CategoriaForm


def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def eliminar_categoria(request, id):
    Categoria.objects.get(id=id).delete()
    return redirect('videojuego:lista')

def nuevo_categoria(request):
    form = CategoriaForm()

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
    context = {'form': form }
    return render(request, 'nuevo_categoria.html', context)

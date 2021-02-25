from django.shortcuts import render, redirect
from .models import Categoria, Videojuego
from .form_categoria import CategoriaForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def eliminar_categoria(request, id):
    Categoria.objects.get(id=id).delete()
    return redirect('categoria:lista')

def nuevo_categoria(request):
    form = CategoriaForm()

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
    context = {'form': form }
    return render(request, 'nuevo_categoria.html', context)

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
    context = {'form': form }
    return render(request, 'editar_categoria.html', context)


class VideojuegoList(ListView):
    model = Videojuego
    # context_object_name = 'videojuegos'
    # extra_context = {
    #     'var1': 'Clases génericas',
    #     'nombre': 'Alex',
    # }
    # queryset = Videojuego.objects.filter(anio=1991)

class VideojuegoEliminar(DeleteView):
    model = Videojuego
    success_url = reverse_lazy('videojuego:lista')

class VideojuegoCrear(CreateView):
    model = Videojuego
    fields = '__all__'
    success_url = reverse_lazy('videojuego:lista')

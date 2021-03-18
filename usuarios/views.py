from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Usuario, Municipio, Estado
from .forms import UsuarioForm
from django.http import JsonResponse


class NuevoUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    success_url = reverse_lazy('videojuego:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        # user.is_active = 0
        # print (user)

        return super().form_valid(form)


def obtiene_municipios(request):
    # estado = get_object_or_404(Estado, id=id_estado)
    if request.method == 'GET':
        return JsonResponse({'error':'Petición incorrecta'}, safe=False,  status=403)
    id_estado = request.POST.get('id')
    municipios = Municipio.objects.filter(estado_id=id_estado)
    json = []
    if not municipios:
        json.append({'error':'No se encontrar municipios para ese estado'})
        
    for municipio in municipios:
        json.append({'id':municipio.id, 'nombre':municipio.nombre})
    return JsonResponse(json, safe=False)


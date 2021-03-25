from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.contrib import messages
from .token import token_activacion
from .forms import UsuarioForm
from .models import Usuario, Municipio, Estado


class NuevoUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta': 'Nuevo', 'boton': 'Agregar'}
    success_url = reverse_lazy('videojuego:lista')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        dominio = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)
        mensaje = render_to_string('confirmar_cuenta.html',
            {
                'usuario': user,
                'dominio': dominio,
                'uid': uid,
                'token': token
            }
        )
        asunto = 'Activa cuenta Videojuegos'
        to = user.email
        email = EmailMessage(
            asunto,
            mensaje,
            to=[to]
        )
        email.content_subtype = 'html'
        email.send()


        return super().form_valid(form)
class ActivarCuenta(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(kwargs['uid64'])
            token = kwargs['token']
            user = Usuario.objects.get(id=uid)
        except:
            user = None

        if user and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(self.request, 'Cuenta activada con éxito')
        else:
            messages.error(self.request, 'Token inválido, contacta al administrador')

        return redirect('usuarios:login')

class ListaUsuario(ListView):
    model = Usuario

class LoginUsuario(LoginView):
    template_name = 'login.html'
    # form_class = AuthenticationForm


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


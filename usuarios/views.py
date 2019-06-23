import random

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponse

from gestion_recursos import settings
from usuarios.forms import SisgerecuAuthenticationForm
from django.urls import reverse_lazy, reverse


# Create your views here.
from usuarios.models import User


class SisgerecuLoginView(LoginView):
    template_name = 'usuarios/login.html'
    form_class = SisgerecuAuthenticationForm
    get_success_url = reverse_lazy('index')

    def form_valid(self, form):
        print(self.request.POST)
        user = form.get_user()
        codigo_verificacion_formulario = form.data['codigo_verificacion']
        codigo_verificacion_bd = User.objects.get(username=self.request.POST.get('username')).codigo_verificacion
        if user is not None:
            if codigo_verificacion_formulario == codigo_verificacion_bd:
                login(self.request, user)
            return HttpResponseRedirect(self.get_success_url)

    def get_context_data(self, **kwargs):
        context = super(SisgerecuLoginView, self).get_context_data(**kwargs)
        return context

class SisgerecuLogoutView(LogoutView):
    template_name = 'usuarios/login.html'
    form_class = SisgerecuAuthenticationForm
    next_page = settings.LOGIN_URL

    def get(self, *args, **kwargs):
        logout(self.request)
        return super(SisgerecuLogoutView, self).get(*args, **kwargs)


def obtener_numero_celular(request, usuario):
    """
    Envia el numero de celular correspondiente al usuario que se recibe
    :param request:
    :param usuario: Usuario registrado en la base de datos
    :return: Numero celualar del usuario
    """
    usuario = User.objects.get(username=usuario)
    numero_celular_usuario = usuario.celular
    codigo_verificacion = generar_codigo_verificacion()
    usuario.codigo_verificacion = codigo_verificacion
    usuario.save()
    enviar_codigo_verificacion(codigo_verificacion, numero_celular_usuario)

    return HttpResponse("%s" % numero_celular_usuario)

def generar_codigo_verificacion():
    """
    Genera codigo de verificacion de 4 digitos
    :return:
    """
    codigo = ""
    for i in range(4):
        codigo = codigo + str(random.randrange(10))
    print(codigo)
    return codigo


def enviar_codigo_verificacion(codigo_verificacion, numero_celular):
    import instasent
    client = instasent.Client('3c0a1c10cd7bb3ea6eef9a46d3a8f26282dbf868')
    mensaje = 'Su codigo de verificación es: %s' % codigo_verificacion
    destinatario = '+57%s' % numero_celular
    response = client.send_sms('Sisgerecu', destinatario, mensaje)
    print(response)
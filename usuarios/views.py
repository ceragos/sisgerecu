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
        cod_verif = self.request.POST.get('cod_verif')
        if user is not None:
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
    numero_celular_usuario = User.objects.get(username=usuario).celular
    return HttpResponse("%s" % numero_celular_usuario)

def generar_codigo_verificacion():
    """
    Genera codigo de verificacion de 4 digitos
    :return:
    """
    codigo = ""
    for i in range(4):
        codigo = codigo + str(random.randrange(10))
    return codigo
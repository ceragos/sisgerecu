from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect

from gestion_recursos import settings
from usuarios.forms import SisgerecuAuthenticationForm
from django.urls import reverse_lazy, reverse


# Create your views here.

class SisgerecuLoginView(LoginView):
    template_name = 'usuarios/login.html'
    form_class = SisgerecuAuthenticationForm
    get_success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.get_user()
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

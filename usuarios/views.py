from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
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
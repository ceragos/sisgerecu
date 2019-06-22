from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from usuarios.models import User


class SisgerecuAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(SisgerecuAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'username', 'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update({'class': 'password', 'placeholder': 'Contraseña'})


class CrearUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('numero_documento', 'first_name', 'last_name', 'celular', 'email', 'username', 'password1', 'password2', 'groups')


class ActualizarUsuarioForm(UserChangeForm):
    # para que no hablite el cambio de contraseña en el formulario frontend
    password = None

    class Meta:
        model = User
        fields = ('numero_documento', 'first_name', 'last_name', 'celular', 'email', 'username', 'groups')
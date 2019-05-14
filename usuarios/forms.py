from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SisgerecuAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(SisgerecuAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'username', 'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update({'class': 'password', 'placeholder': 'Contraseña'})


class CrearUsuarioForm(UserCreationForm):
    pass
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from usuarios.models import User


class SisgerecuAuthenticationForm(AuthenticationForm):
    codigo_verificacion = forms.CharField(label='Codigo de verificación', max_length=4)

    def __init__(self, *args, **kwargs):
        super(SisgerecuAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'username', 'placeholder': 'User'})
        self.fields['password'].widget.attrs.update({'class': 'password', 'placeholder': 'Contraseña'})
        self.fields['codigo_verificacion'].widget.attrs.update({'class': 'codigo_verificacion',
                                                                'placeholder': 'Codigo de verificación'})

    def clean_codigo_verificacion(self):
        codigo_verificacion = self.cleaned_data['codigo_verificacion']
        usuario = User.objects.get(username=self.cleaned_data['username'])
        if not codigo_verificacion == usuario.codigo_verificacion:
            raise ValidationError('Codigo de verificación invalido')

        if now() > usuario.fecha_solicitud_codigo_verificacion + timedelta(minutes=5):
            raise ValidationError('Codigo de verificación vencido')

        return codigo_verificacion


class CrearUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('numero_documento', 'first_name', 'last_name', 'celular', 'email', 'username', 'password1',
                  'password2', 'groups')


class ActualizarUsuarioForm(UserChangeForm):
    # para que no habilite el cambio de contraseña en el formulario frontend
    password = None

    class Meta:
        model = User
        fields = ('numero_documento', 'first_name', 'last_name', 'celular', 'email', 'username', 'groups')


class PerfilUsuarioForm(UserChangeForm):
    # para que no habilite el cambio de contraseña en el formulario frontend
    password = None

    class Meta:
        model = User
        fields = ('foto_perfil', 'first_name', 'last_name', 'celular', 'email')

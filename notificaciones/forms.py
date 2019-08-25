from django import forms

from notificaciones.models import ComunicacionInterna


class ComunicacionInternaForm(forms.ModelForm):
    class Meta:
        model = ComunicacionInterna
        fields = ['reserva', 'remitente', 'destinatario', 'mensaje']
        widgets = {
            'reserva': forms.Select(attrs={'class': 'form-control'}),
            'remitente': forms.Select(attrs={'class': 'form-control'}),
            'destinatario': forms.Select(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ComunicacionInternaForm, self).__init__(*args, **kwargs)

    def clean_remitente(self):
        self.instance.estado = True
        return self.user

    def clean_destinatario(self):
        reserva = self.cleaned_data['reserva']
        return reserva.usuario

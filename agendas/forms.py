from datetime import date, time
from django import forms

from agendas.models import Agenda


class CustomTimeInput(forms.TimeInput):
    input_type = 'time'


class AgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda
        exclude = ['usuario']
        fields = ['recurso_fisico', 'recurso_tecnologico', 'fecha_separacion', 'hora_separacion', 'fecha_devolucion',
                  'hora_devolucion']
        widgets = {
            'recurso_fisico': forms.Select(attrs={'class': 'form-control'}),
            'recurso_tecnologico': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fecha_separacion': forms.SelectDateWidget(attrs={'class': 'form-control',
                                                              'style': 'display: inline; width: 32.8%;'},
                                                       years=range(date.today().year,
                                                                   date.today().year+1)),
            'hora_separacion': CustomTimeInput,
            'fecha_devolucion': forms.SelectDateWidget(attrs={'class': 'form-control',
                                                              'style': 'display: inline; width: 32.8%;'},
                                                       years=range(date.today().year,
                                                                   date.today().year+1)),
            'hora_devolucion': CustomTimeInput,
        }

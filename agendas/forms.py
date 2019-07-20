from datetime import date
from django import forms

from agendas.models import Agenda
from recursos.models import RecursoTecnologico


class CustomTimeInput(forms.TimeInput):
    input_type = 'time'


class AgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda
        exclude = ['usuario']
        fields = ['recurso_fisico', 'recurso_tecnologico', 'fecha_separacion', 'hora_separacion',
                  'hora_devolucion']
        widgets = {
            'recurso_fisico': forms.Select(attrs={'class': 'form-control'}),
            'recurso_tecnologico': forms.CheckboxSelectMultple(attrs={'class': 'form-control'}),
            'fecha_separacion': forms.SelectDateWidget(attrs={'class': 'form-control',
                                                              'style': 'display: inline; width: 32.8%;'},
                                                       years=range(date.today().year,
                                                                   date.today().year + 1)),
            'hora_separacion': CustomTimeInput,
            'hora_devolucion': CustomTimeInput,
        }

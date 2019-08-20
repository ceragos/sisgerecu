from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q

from agendas.models import Agenda


class CustomTimeInput(forms.TimeInput):
    input_type = 'time'


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ['usuario']
        fields = ['fecha_separacion', 'hora_separacion', 'hora_devolucion', 'recurso_fisico', 'recurso_tecnologico']
        widgets = {
            'recurso_fisico': forms.Select(attrs={'class': 'form-control'}),
            'recurso_tecnologico': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'fecha_separacion': forms.SelectDateWidget(attrs={'class': 'form-control',
                                                              'style': 'display: inline; width: 32.8%;'},
                                                       years=range(date.today().year,
                                                                   date.today().year + 2)),
            'hora_separacion': CustomTimeInput,
            'hora_devolucion': CustomTimeInput,
        }

    def clean_hora_devolucion(self):
        hora_devolucion = self.cleaned_data['hora_devolucion']
        hora_separacion = self.cleaned_data['hora_separacion']

        if hora_separacion > hora_devolucion:
            raise ValidationError('Esta hora no puede ser anterior a la hora de separación')

        if hora_separacion == hora_devolucion:
            raise ValidationError('Esta hora no puede ser igual a la hora de separación')

        return hora_devolucion

    def clean_recurso_fisico(self):
        recurso_fisico = self.cleaned_data['recurso_fisico']
        fecha_separacion = self.cleaned_data['fecha_separacion']
        hora_separacion = self.cleaned_data['hora_separacion']
        hora_devolucion = self.cleaned_data['hora_devolucion']

        # Consulta de los elementos existentes en el mismo horario
        agenda_dia = Agenda.objects.filter(fecha_separacion=fecha_separacion)
        agenda_dia = agenda_dia.filter(Q(hora_separacion__range=(hora_separacion, hora_devolucion))
                                       | Q(hora_devolucion__range=(hora_separacion, hora_devolucion)))

        # Validación realizada para excluir si es una instancia de si misma, y así queda habilitada para hacer edición
        if self.instance:
            agenda_dia = agenda_dia.exclude(pk=self.instance.pk)

        # Validación de disponibilidad
        for agenda in agenda_dia:
            if recurso_fisico == agenda.recurso_fisico:
                raise ValidationError('El {} ya fue agendado desde las {} hasta las {} por {}'.format(
                    recurso_fisico,
                    agenda.hora_separacion.strftime('%I:%M %p'),
                    agenda.hora_devolucion.strftime('%I:%M %p'),
                    agenda.usuario))

        return recurso_fisico

    def clean_recurso_tecnologico(self):
        recurso_tecnologico = self.cleaned_data['recurso_tecnologico']
        fecha_separacion = self.cleaned_data['fecha_separacion']
        hora_separacion = self.cleaned_data['hora_separacion']
        hora_devolucion = self.cleaned_data['hora_devolucion']

        # Consulta de los elementos existentes en el mismo horario
        agenda_dia = Agenda.objects.filter(fecha_separacion=fecha_separacion)
        agenda_dia = agenda_dia.filter(Q(hora_separacion__range=(hora_separacion, hora_devolucion))
                                       | Q(hora_devolucion__range=(hora_separacion, hora_devolucion)))

        # Validación realizada para excluir si es una instancia de si misma, y así queda habilitada para hacer edición
        if self.instance:
            agenda_dia = agenda_dia.exclude(pk=self.instance.pk)

        # Validación de disponibilidad
        for agenda in agenda_dia:
            for recurso in recurso_tecnologico:
                if recurso in agenda.recurso_tecnologico.all():
                    raise ValidationError('El {} ya fue agendado desde las {} hasta las {} por {}'.format(
                        recurso,
                        agenda.hora_separacion.strftime('%I:%M %p'),
                        agenda.hora_devolucion.strftime('%I:%M %p'),
                        agenda.usuario))

        return recurso_tecnologico


class FechaForm(forms.Form):
    fecha = forms.DateField(required=False)

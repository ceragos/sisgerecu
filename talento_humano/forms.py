import datetime

from django import forms

from talento_humano.models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento', 'celular', 'correo_electronico', 'fecha_ingreso',
                  'titulo_obtenido', 'carrera_profesional', 'perfil']
        widgets = {
            'numero_documento': forms.TextInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.SelectDateWidget(attrs={'class': 'form-control', 'style':'display:inline;width:32.8%;'},
                                                       years=range(1919, datetime.date.today().year-15)),
            'celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.SelectDateWidget(attrs={'class': 'form-control', 'style':'display:inline;width:32.8%;'},
                                                    years=range(datetime.date.today().year-20, datetime.date.today().year+2)),
            'titulo_obtenido': forms.Select(attrs={'class': 'form-control'}),
            'carrera_profesional': forms.Select(attrs={'class': 'form-control'}),
            'perfil': forms.Select(attrs={'class': 'form-control'}),
        }

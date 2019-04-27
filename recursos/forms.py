from django import forms

from recursos.models import RecursoFisico, RecursoTecnologico


class RecursoFisicoForm(forms.ModelForm):

    class Meta:
        model = RecursoFisico
        fields = ['tipo_aula', 'numero', 'ubicacion', 'capacidad', 'caracteristicas', 'contenido']
        widgets = {
            'tipo_aula': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristicas': forms.Textarea(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        }

class RecursoTecnologicoForm(forms.ModelForm):

    class Meta:
        model = RecursoTecnologico
        fields = fields = ['tipo_equipo', 'numero', 'marca', 'referencia', 'color', 'caracteristicas', 'contenido']
        widgets = {
            'tipo_equipo': forms.Select(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'caracteristicas': forms.Textarea(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        }
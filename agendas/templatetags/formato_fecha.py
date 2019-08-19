from django.template import Library

register = Library()


@register.filter
def formato_12_horas(hora):
    return hora.strftime('%I:%M %p')

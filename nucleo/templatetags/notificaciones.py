from django.template import Library

register = Library()


@register.filter
def contador(objeto):
    return objeto.filter(estado=False).count()

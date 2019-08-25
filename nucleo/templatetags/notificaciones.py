from django.template import Library

register = Library()


@register.filter
def comunicaciones_no_leidas(objeto):
    return objeto.filter(estado=False).count()

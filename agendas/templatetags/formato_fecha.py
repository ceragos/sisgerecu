from django.template import Library

register = Library()


@register.filter
def formato_12_horas(hora):
    return hora.strftime('%I:%M %p')


@register.filter
def validar_botones_agenda(reserva):
    """
    valida que la fecha de reserva no sea anterior a la actual
    :return:
    """
    import datetime
    fecha_hora_reserva = datetime.datetime.combine(reserva.fecha_separacion, reserva.hora_separacion)
    fecha_hora_actual = datetime.now()
    if fecha_hora_reserva < fecha_hora_actual:
        return False
    return True

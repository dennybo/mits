import re
from django import template

register = template.Library()


urlfinder = re.compile('^(https?:\/\/\S+)')
urlfinder2 = re.compile('\s(https?:\/\/\S+)')


@register.filter
def urlfy(value):
    value = value.replace("<", "&lt;")
    value = value.replace(">", "&gt;")
    value = urlfinder.sub(r'<\1>', value)
    value = urlfinder2.sub(r' <\1>', value)
    return value

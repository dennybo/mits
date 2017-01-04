import re
from django import template

register = template.Library()


urlfinder = re.compile('^(https?:\/\/\S+)')
urlfinder2 = re.compile('\s(https?:\/\/\S+)')


@register.filter
def urlfy(value):
    value = urlfinder.sub(r'<\1>', value)
    return urlfinder2.sub(r' <\1>', value)

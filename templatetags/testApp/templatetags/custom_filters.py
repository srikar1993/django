from django import template

register = template.Library()

@register.filter(name = 'alt_upper')
def alternate_upper(value):
    return value[0::2].upper()

@register.filter(name = 'trunc_n')
def truncate_n(value, n):
    return value[:n]

# @register.filter(name = 'n_trunc')
# def n_truncate_n(value, x ,y):
#     return value[x:y]

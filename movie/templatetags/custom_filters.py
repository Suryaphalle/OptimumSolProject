from django import template

register = template.Library()

@register.filter
def to_list(value, arg):
    return range(int(arg))
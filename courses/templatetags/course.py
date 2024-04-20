from django import template

register = template.Library()


def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
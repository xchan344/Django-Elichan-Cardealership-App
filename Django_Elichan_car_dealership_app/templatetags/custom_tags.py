from django import template

register = template.Library()

@register.filter
def add_attr(field, attr):
    return field.as_widget(attrs={'type': attr})
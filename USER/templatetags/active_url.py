from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag
def is_active(request, url_name):
    try:
        if request.path == reverse(url_name):
            return 'active'
    except NoReverseMatch:
        pass
    return ''

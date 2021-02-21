from django import template
from ..models import Slider

register = template.Library()


@register.simple_tag
def get_slider():
    return Slider.objects.all().first().adverts.all()
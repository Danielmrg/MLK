from django import template
import itertools

register = template.Library()

@register.filter
def my_grouper(iterable,num):
    args = [iter(iterable)]*num
    return ([e for e in t if e != None] for t in itertools.zip_longest(*args))
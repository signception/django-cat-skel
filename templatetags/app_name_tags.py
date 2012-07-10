#-*- coding: UTF-8 -*-
from django import template

register = template.Library()

#@register.inclusion_tag('/{{app_name}}/tags/my_tag.html)
#def my_tag():
#    pass

#@register.inclusion_tag('/{{app_name}}/tags/my_tag.html', takes_context=True)
#def my_tag_with_context(context):
#    pass
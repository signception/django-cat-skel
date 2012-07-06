#-*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.admin.options import TabularInline, StackedInline

from .models import *

def inline_factory(m, parent_class=TabularInline):
    class helper(parent_class):
        model = m
    return helper

class {{app_name|capfirst}}ItemAdmin(admin.ModelAdmin):
    inlines = [
        inline_factory({{app_name|capfirst}}ItemImage),
    ]
    ordering = ['order',]
    list_display = ('title', 'order',)

admin.site.register({{app_name|capfirst}}Item, {{app_name|capfirst}}ItemAdmin)
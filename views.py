#-*- coding: UTF-8 -*-
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *

class {{app_name|capfirst}}ItemListView(ListView):
    model = {{app_name|capfirst}}Item
    context_object_name='items'
    template_name = '{{app_name}}/list.html'

    def get_queryset(self):
        return super({{app_name|capfirst}}ItemListView, self).get_queryset().order_by('order')


class {{app_name|capfirst}}ItemDetailView(DetailView):
    model = {{app_name|capfirst}}Item
    context_object_name='item'
    template_name = '{{app_name}}/item.html'
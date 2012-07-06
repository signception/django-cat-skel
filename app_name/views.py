#-*- coding: UTF-8 -*-
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *

class {{app_name|capfirst}}ItemListView(ListView):
    model = {{app_name|capfirst}}Item
    context_object_name='items'

    def get_queryset(self):
        return super({{app_name|capfirst}}Item, self).get_queryset().order_by('order')


class {{app_name|capfirst}}ItemDetailView(DetailView):
    model = {{app_name|capfirst}}Item
    context_object_name='item'
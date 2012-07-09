#-*- coding: UTF-8 -*-
from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from .models import {{app_name|capfirst}}Item

class {{app_name|capfirst}}Menu(CMSAttachMenu):
    name = u'{{app_name}} menu'

    def get_nodes(self, request):
        nodes = []

        for item in {{app_name|capfirst}}Item.objects.all():
            nodes.append(NavigationNode(item.title,
                                        item.get_absolute_url(),
                                        item.pk))

        return nodes

menu_pool.register_menu({{app_name|capfirst}}Menu) # register the menu
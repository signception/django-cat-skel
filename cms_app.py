#-*- coding: UTF-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import {{app_name|capfirst}}Menu

class {{app_name|capfirst}}Apphook(CMSApp):
    name = u'{{app_name|capfirst}} app hook'
    urls = ['{{app_name}}.urls']
    menus = [{{app_name|capfirst}}Menu]

apphook_pool.register({{app_name|capfirst}}Apphook)
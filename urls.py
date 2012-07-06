from django.conf.urls import patterns, url

from .models import *
from .views import *

urlpatterns = patterns('',
    url(r'^$', {{app_name|capfirst}}ItemListView.as_view()),

    url(r'^(?P<pk>\d+)/$', {{app_name|capfirst}}ItemDetailView.as_view(model={{app_name|capfirst}}Item,
        context_object_name='project'),
        name='{{app_name}}_item')
)
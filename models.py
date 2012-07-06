#-*- coding: UTF-8 -*-
from django.db.models import permalink
import os
from datetime import datetime
from django.db import models
from tinymce import models as tinymce_models
import pytils


def _create_image_path(_, filename):
    now = datetime.now()
    date_path = now.strftime('{{app_name}}/%Y/%m/%d/')
    filename_slug = pytils.translit.translify(filename)
    return os.path.join(date_path, filename_slug)


class {{app_name|capfirst}}Item(models.Model):
    title = models.CharField(max_length=100)

    # consider if you need only one image or multiple images
    image = models.ImageField(upload_to=_create_image_path)

    description = tinymce_models.HTMLField(blank=True)

    order = models.IntegerField(default=0, blank=True)

    def get_next(self):
        try:
            return {{app_name|capfirst}}Item.objects.filter(order__gt=self.order).order_by('order')[0]
        except IndexError:
            return None

    def get_prev(self):
        try:
            return {{app_name|capfirst}}Item.objects.filter(order__lt=self.order).order_by('-order')[0]
        except IndexError:
            return None

    @permalink
    def get_absolute_url(self):
        return '{{app_name}}_item', [self.id]

    def __unicode__(self):
        return self.title

#    class Meta:
#        verbose_name = u'Item'
#        verbose_name_plural = u'Items'


class {{app_name|capfirst}}ItemImage(models.Model):
    {{app_name}}_item = models.ForeignKey({{app_name|capfirst}}Item, related_name='images')
    image = models.ImageField(upload_to=_create_image_path)

    title = models.CharField(max_length=100)
    description = tinymce_models.HTMLField(blank=True)

    def __unicode__(self):
        return self.title

#    class Meta:
#        verbose_name = u'Image'
#        verbose_name_plural = u'Images'
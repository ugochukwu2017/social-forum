from django import template
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html_join

from ..models import Tag


register = template.Library()


@register.simple_tag(takes_context=True)
def tagcloud(context, owner=None):
    url = reverse('booz_list')
    filters = {'booz__is_public': True}

    if owner is not None:
        url = reverse('booz_user',
            kwargs={'username': owner.username})
        filters['booz__owner'] = owner
    if context['user'] == owner:
        del filters['booz__is_public']

    tags = Tag.objects.filter(**filters)
    tags = tags.annotate(count=models.Count('booz'))
    tags = tags.order_by('name').values_list('name', 'count')
    fmt = '<a href="%s?tag={0}">{0} ({1})</a>' % url
    return format_html_join(', ', fmt, tags)

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ImproperlyConfigured

def getid():
    from simpleflake import simpleflake
    return simpleflake()

from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


class GenericSimpleflakeIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    object_id = models.BigIntegerField(verbose_name=_('Object id'), db_index=True)
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class BaseModel(models.Model):
    id = models.BigIntegerField(
        _('id'),
        primary_key=True,
        editable=False,
        default=getid
    )
    created = models.DateTimeField(_('creation time'), auto_now_add=True)
    modified = models.DateTimeField(_('last modification time'), auto_now=True)

    # Store it in depot, if it's not a foreign key, or a piece
    # of data that absolutely must be a separate field.
    depot = JSONField(_('JSON Depot'), default={}, blank=True)

    class Meta:
        abstract = True

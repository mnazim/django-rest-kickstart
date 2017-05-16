from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ImproperlyConfigured

def getid():
    from simpleflake import simpleflake
    return simpleflake()


class BaseModel(models.Model):
    id = models.BigIntegerField(
        _('id'),
        primary_key=True,
        editable=False,
        default=getid
    )
    created = models.DateTimeField(_('creation time'), auto_now_add=True)
    modified = models.DateTimeField(_('last modification time'), auto_now=True)
    depot = JSONField(_('JSON Depot'), default={}, blank=True)

    class Meta:
        abstract = True

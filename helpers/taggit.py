from django.db import models
from django.utils.translation import ugettext as _
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


class GenericSimpleflakeIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    object_id = models.BigIntegerField(verbose_name=_('Object id'), db_index=True)

    class Meta:
        abstract = True

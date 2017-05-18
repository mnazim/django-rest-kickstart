from django.db import models
from django_extensions.db.fields import AutoSlugField
from model_utils.fields import StatusField
from model_utils import Choices
from taggit.managers import TaggableManager
from helpers.models import BaseModel
from django.conf import settings


class Thing(BaseModel):

    name = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from=['name'], max_length=256)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='things',
        null=True,
        blank=True
    )

    STATUS = Choices('draft', 'published')
    status = StatusField(choices_name='STATUS')

    KINDS = Choices('cake', 'cookie', 'candy')
    kind = StatusField(choices_name='KINDS')

    tags = TaggableManager(through='helpers.GenericSimpleflakeIDTaggedItem')

    class Meta:
        db_table = 'things'

    def __str__(self):
        return self.slug

    def is_owned_by(self, user):
        return self.owner == user

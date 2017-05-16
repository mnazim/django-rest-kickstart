from django.db import models
from django_extensions.db.fields import AutoSlugField
from helpers.models import BaseModel


class Thing(BaseModel):
    name = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from=['name'], max_length=256)

    class Meta:
        db_table = 'things'

    def __str__(self):
        return self.slug
